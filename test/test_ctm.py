from tno.etm_price_profile_adapter.model.ctm import CTM
from tno.etm_price_profile_adapter.types import CTMConfig, CTMAdapterConfig
from dotenv import load_dotenv

load_dotenv(verbose = True)

ctm_config = CTMConfig(
    endpoint="https://beta.carbontransitionmodel.com/api/",
    CTM_scenario_ID="base",
    ETM_scenario_ID="13579"
    #bucket=N.A.
)

ctm_adapter_config = CTMAdapterConfig(
    ctm_config=ctm_config,
    output_file_name="file.esdl"
    # output_file_path=None,
    # base_path=None,
)

ctm_config_1 = CTMConfig(
    endpoint="https://beta.carbontransitionmodel.com/api/",
    ETM_session_ID = 'sessionID'
    #bucket=N.A.
)

ctm_adapter_config_1 = CTMAdapterConfig(
    ctm_config=ctm_config,
    output_file_name="file.esdl"
    # output_file_path=None,
    # base_path=None,
)

ctm = CTM()
model_run_info = ctm.request()
model_run_info = ctm.initialize(model_run_id=model_run_info.model_run_id, config=ctm_adapter_config)
model_run_info = ctm.run(model_run_id=model_run_info.model_run_id)
model_run_info = ctm.results(model_run_id=model_run_info.model_run_id)
model_run_info = ctm.initialize(model_run_id=model_run_info.model_run_id, config=ctm_adapter_config_1)
result = model_run_info.result
print(result)


class  ():
    self.model_run_repository = {'model_run_id_1':config, 'model_run_id_2':config, 'model_run_id_3':config,}

# need to work on results handling --> for now the adapter just does what it is supposed to do and returns nothing if all is well --> want some logging of how the run went
