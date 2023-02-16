from tno.etm_price_profile_adapter.model.ctm import CTM
from tno.etm_price_profile_adapter.types import CTMConfig, CTMAdapterConfig

ctm_config = CTMConfig(
    endpoint="https://beta.carbontransitionmodel.com/api/",
    CTM_scenario_ID="base",
    ETM_scenario_ID="13579"
    #bucket=N.A.
)

ctm_adapter_config = CTMAdapterConfig(
    ctm_config=ctm_config,
    input_file_name="MapEditorMesoCasev04_run_2.esdl",
    output_file_name = "MapEditorMesoCasev04_run_2-output.esdl",
    bucket_name="esdl"
    # output_file_path=None,
    # base_path=None,
)

ctm = CTM()
model_run_info = ctm.request()
model_run_info = ctm.initialize(model_run_id=model_run_info.model_run_id, config=ctm_adapter_config)
model_run_info = ctm.run(model_run_id=model_run_info.model_run_id)
model_run_info = ctm.results(model_run_id=model_run_info.model_run_id)

result = model_run_info.result
print(result)
