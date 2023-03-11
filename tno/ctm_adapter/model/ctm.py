import os

from esdl import esdl
import requests

from tno.ctm_adapter.model.model import Model, ModelState
from tno.ctm_adapter.types import CTMAdapterConfig, ModelRunInfo
from tno.ctm_adapter.model.ctm_io import read_inputs, write_inputs
from tno.shared.log import get_logger

logger = get_logger(__name__)


class CTM(Model):

    def process_results(self, result):
        if self.minio_client:
            return result
        else:
            return result

    def run(self, model_run_id: str):
        model_run_info = Model.run(self, model_run_id=model_run_id)        # Uses the model.py run function to make ModelSTATE = "RUNNING"

        if model_run_info.state == ModelState.ERROR:
            return model_run_info

        config: CTMAdapterConfig = self.model_run_dict[model_run_id].config

        ctm_url = config.ctm_config.endpoint
        if self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID == None:
            # Generate the CTM session ID
            logger.info("No CTM session ID found, generate new session ID based on scenario ID")
            jsn = {'ScenarioID': config.ctm_config.CTM_scenario_ID, 'outputs':['SessionID']}
            ctm_out = requests.post(url=ctm_url, json=jsn)
            if ctm_out.status_code == 200:
                ctm_out = ctm_out.json()
                ctm_sess_id = ctm_out['SessionID']
                self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID = ctm_sess_id
            else:
                return ModelRunInfo(
                    model_run_id=model_run_id,
                    state=ModelState.ERROR,
                    reason=f"Error in CTM.run(): CTM session ID could not be generated: {ctm_out.status_code} {ctm_out.reason}"
                )

            # Couple the ETM and CTM
            logger.info("Couple the ETM and CTM")
            ctm_in = {'etm_saved_scenario_id': config.ctm_config.ETM_scenario_ID, 'etm_coupling_switch': 1}
            jsn = {'SessionID': ctm_sess_id, 'inputs': ctm_in, 'outputs': ['etm_session_id']}
            ctm_out = requests.post(url=ctm_url, json=jsn)
            if ctm_out.status_code == 200:
                ctm_out = ctm_out.json()
                etm_sess_id = str(int(ctm_out['output_values']['etm_session_id']))
                self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID = etm_sess_id    #CHECK! should add CTM session ID to model run information
            else:
                return ModelRunInfo(
                    model_run_id=model_run_id,
                    state=ModelState.ERROR,
                    reason=f"Error in CTM.run(): CTM could not couple with specified ETM session ID: {ctm_out.status_code} {ctm_out.reason}"
                )
            logger.info(f"CTM session ID: {ctm_sess_id}, ETM session ID: {etm_sess_id}")
        else:
            ctm_sess_id = self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID
            logger.info(f"CTM session ID already configured: {ctm_sess_id}")
            if self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID:
                ctm_in = {'etm_session_id': self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID, 'etm_coupling_switch': 1}
                jsn = {'SessionID': ctm_sess_id, 'inputs': ctm_in, 'outputs':' etm_session_id'}
                ctm_out = requests.post(url=ctm_url, json=jsn)
                if ctm_out.status_code == 200:
                    ctm_out = ctm_out.json()
                    etm_sess_id = str(int(ctm_out['output_values']['etm_session_id']))
                    if etm_sess_id != self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID:
                        return ModelRunInfo(
                            model_run_id=model_run_id,
                            state=ModelState.ERROR,
                            reason=f"Error in CTM.run(): CTM could not couple with specified ETM session ID: {ctm_out.status_code} {ctm_out.reason}"
                        )
                else:
                    return ModelRunInfo(
                        model_run_id=model_run_id,
                        state=ModelState.ERROR,
                        reason=f"Error in CTM.run(): CTM could not couple with specified ETM session ID: {ctm_out.status_code} {ctm_out.reason}"
                    )
            else:
                logger.error("ETM session ID is not found")
                return ModelRunInfo(
                        model_run_id=model_run_id,
                        state=ModelState.ERROR,
                        reason=f"Error in CTM.run(): ETM_session_ID is not found"
                    )

        # Now we have prepared the session IDs that we will work with
        if self.minio_client:
            logger.info("Load ESDL file from Minio")
            input_esdl_bytes = self.load_from_minio(config.base_path + '/' + config.input_esdl_file_path)
        else:
            logger.info("Load ESDL file from file system")
            input_path = os.path.join(config.base_path, config.input_esdl_file_path)
            with open(input_path, "rb") as input_file:
                input_esdl_bytes = input_file.read()
        input_esdl = input_esdl_bytes.decode('utf-8')

        logger.info("Read inputs from ESDL and send to CTM")
        ctm_in = read_inputs(
            {esdl.Electrolyzer: "esdl.Electrolyzer.csv", esdl.GasConversion: "esdl.GasConversion.csv"},
            input_esdl
        )
        # print(ctm_in, end='\n\n\n')
        ctm_in["etm_session_id"] = etm_sess_id
        jsn = {
            'SessionID': self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID,
            'inputs': ctm_in,
            'outputs': []
        }
        requests.post(url=ctm_url, json=jsn)

        logger.info("Retrieve results from CTM")
        out = requests.post(
            url=ctm_url,
            json={
                'SessionID': self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID,
                'outputs': ['yara_production_h2_smr','yara_production_h2_electrolysis'],
                'inputs':{}
            }
        )

        esdl_str =  write_inputs({esdl.Electrolyzer:"esdl.Electrolyzer.csv", esdl.GasConversion:"esdl.GasConversion.csv"}, input_esdl, self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, self.model_run_dict[model_run_id].config.ctm_config.endpoint)
        model_run_info = Model.store_result(self, model_run_id=model_run_id, result=esdl_str)

        if not self.minio_client:
            with open(os.path.join(config.base_path, config.output_esdl_file_path), "w") as out_file:
                out_file.write(self.model_run_dict[model_run_id].result['result'])

        self.model_run_dict[model_run_id].result['ctm_session_id'] = self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID
        self.model_run_dict[model_run_id].result['etm_session_id'] = etm_sess_id

        return model_run_info

    def results(self, model_run_id: str):
        if model_run_id in self.model_run_dict:
            return ModelRunInfo(
                state=self.model_run_dict[model_run_id].state,
                model_run_id=model_run_id,
                result=self.model_run_dict[model_run_id].result,
            )
        else:
            return ModelRunInfo(
                model_run_id=model_run_id,
                state=ModelState.ERROR,
                reason="Error in Model.results(): model_run_id unknown"
            )