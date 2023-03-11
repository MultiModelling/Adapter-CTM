from tno.ctm_adapter.model.ctm import CTM
from tno.ctm_adapter.types import CTMConfig, CTMAdapterConfig
from dotenv import load_dotenv

load_dotenv(verbose=True)

ctm_config = CTMConfig(
    endpoint="https://beta.carbontransitionmodel.com/api/",
    CTM_scenario_ID="base",
    ETM_scenario_ID="13579"
)

ctm_adapter_config = CTMAdapterConfig(
    ctm_config=ctm_config,
    base_path="files",
    # base_path="meso",
    input_esdl_file_path="input_file.esdl",
    output_esdl_file_path="output_file.esdl",
)

ctm = CTM()
model_run_info = ctm.request()
model_run_info = ctm.initialize(model_run_id=model_run_info.model_run_id, config=ctm_adapter_config)
model_run_info = ctm.run(model_run_id=model_run_info.model_run_id)
model_run_info = ctm.results(model_run_id=model_run_info.model_run_id)
print(model_run_info)
result = model_run_info.result
print(result)
