from dataclasses import dataclass
from typing import Optional
from esdl import esdl
import requests

from tno.etm_price_profile_adapter.model.model import Model, ModelState
from tno.etm_price_profile_adapter.types import CTMAdapterConfig, ModelRunInfo
from specific_adapter.f import read_inputs, write_inputs


class CTM(Model):

    def process_results(self, result):
        if self.minio_client:
            return result
        else:
            # want to return esdl file
            #return curve_values
            pass

    def run(self, model_run_id: str):
        res = Model.run(self, model_run_id=model_run_id)        # Uses the model.py run function to make ModelSTATE = "RUNNING"

        if model_run_id in self.model_run_dict:
            config: CTMAdapterConfig = self.model_run_dict[model_run_id].config
            ctm_url = config.ctm_config.endpoint

# config will contain:
# endpoint: str
# CTM_scenario_ID: str
# ETM_scenario_ID: str
# output_file_name: str
# Now, what we want to do first is generate the CTM session ID we will be working on (line 32 to
            if self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID and self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID:
                    ctm_in = {'etm_session_id':self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID, 'etm_coupling_switch':1}
                    jsn = {'SessionID':self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, 'inputs':ctm_in, 'outputs':'etm_session_id'}
                    ctm_out = requests.post(url = ctm_url, json = jsn)
                    ctm_out = ctm_out.json()
                    etm_sess_id = ctm_out['output_values']['etm_session_id']
                    if etm_sess_id != self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID:
                        return ModelRunInfo(
                            model_run_id=model_run_id,
                            state=ModelState.ERROR,
                            reason=f"Error in CTM.run(): CTM could not couple with specified ETM session ID: {response.status_code} {response.reason}"
                        )
            elif self.model_run_dict[model_run_id].config.ctm_config.CTM_scenario_ID and self.model_run_dict[model_run_id].config.ctm_config.ETM_scenario_ID:
                jsn = {'ScenarioID':config.ctm_config.CTM_scenario_ID, 'outputs':['SessionID']}
                ctm_out = requests.post(url = ctm_url, json = jsn)
                ctm_out = ctm_out.json()        # if CTM scenario ID is not valid this will kick an error --> maybe implement clear error instructions with try/excpt
                ctm_sess_id = ctm_out['SessionID']
                self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID = ctm_sess_id    #CHECK! should add CTM session ID to model run information
            
# Next, we want to couple the ETM and CTM together
                ctm_in = {'etm_saved_scenario_id':config.ctm_config.ETM_scenario_ID, 'etm_coupling_switch':1, 'bin_etm_pro':1}
                jsn = {'SessionID':ctm_sess_id, 'inputs':ctm_in, 'outputs':['etm_session_id']}
                print(jsn)
                ctm_out = requests.post(url = ctm_url, json = jsn)
                ctm_out = ctm_out.json()
                etm_sess_id = ctm_out['output_values']['etm_session_id']
                self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID = etm_sess_id    #CHECK! should add CTM session ID to model run information
            else:
                return ModelRunInfo(
                    model_run_id=model_run_id,
                    state=ModelState.ERROR,
                    reason=f"Error in CTM.run(): CTM could not couple ETM and CTM because not both ETM and CTM session or scenario IDs were given: {response.status_code} {response.reason}"
                )


# Now we have prepared the session IDs that we will work with
            if self.minio_client:
                esdl_rel_path = 'files/' + self.model_run_dict[model_run_id].config.output_file_name
                self.minio_client.fget_object(self.model_run_dict[model_run_id].config.bucket_name, self.model_run_dict[model_run_id].config.output_file_name, esdl_rel_path) # yes?
            else:
                esdl_rel_path = self.model_run_dict[model_run_id].config.output_file_name     # so, if minio not deployed, make sure to run the test from the same folder where you keep the esdl file
            
            ctm_in = read_inputs({esdl.Electrolyzer:"esdl.Electrolyzer.csv", esdl.GasConversion:"esdl.GasConversion.csv"}, esdl_rel_path)
            ctm_in["etm_session_id"] = etm_sess_id
            jsn = {'SessionID':self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, 'inputs':ctm_in, 'outputs':[]}
            requests.post(url = ctm_url, json = jsn)
            
            #print(self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, end='\n')
            
            #print({'SessionID':self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, 'outputs':['yara_production_h2_smr','yara_production_h2_electrolysis'], 'inputs':{}}, end='\n')
            
            #out = requests.post(url = ctm_url, json = {'SessionID':self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, 'outputs':['yara_production_h2_smr','yara_production_h2_electrolysis'], 'inputs':{}})
            
            #print(out.json())
            print(self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID)
            write_inputs({esdl.Electrolyzer:"esdl.Electrolyzer.csv", esdl.GasConversion:"esdl.GasConversion.csv"}, esdl_rel_path, self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, self.model_run_dict[model_run_id].config.ctm_config.endpoint)
                
            if self.minio_client:
                file_location = 'files/' + self.model_run_dict[model_run_id].config.output_file_name
                file_name_out = self.model_run_dict[model_run_id].config.output_file_name + 'post_ctm'
                self.minio_client.fput_object(self.model_run_dict[model_run_id].config.bucket_name, file_name_out, file_location)
                self.model_run_dict[model_run_id].result = {'output file':file_name_out , 'output bucket':self.model_run_dict[model_run_id].config.bucket_name, 'CTM session ID':self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID , 'ETM session ID':self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID}
            else:
                self.model_run_dict[model_run_id].result = {'output file':file_name_out, 'CTM session ID':self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID, 'ETM session ID':self.model_run_dict[model_run_id].config.ctm_config.ETM_session_ID}
            
            print(self.model_run_dict[model_run_id].config.ctm_config.CTM_session_ID)
            
            
            
            return ModelRunInfo(
                model_run_id=model_run_id,
                state=ModelState.SUCCEEDED,
            )

        else:
            return ModelRunInfo(
                model_run_id=model_run_id,
                state=ModelState.ERROR,
                reason="Error in CTM.run(): model_run_id unknown"
            )

