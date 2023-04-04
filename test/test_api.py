import requests

api_endpoint = "http://localhost:9205"
#api_endpoint = "http://adapter-ctm:9205"


res = requests.get(api_endpoint + '/status')
if res.ok:
    print("Endpoint /status ok! ", res)
else:
    print("Endpoint /status not ok! ")
    exit(1)

model_run_id = None
res = requests.get(api_endpoint + '/model/request')
if res.ok:
    print("Endpoint /model/request ok!")
    result = res.json()
    print(result)
    model_run_id = result['model_run_id']
else:
    print("Endpoint /model/request not ok!")
    exit(1)

post_body = {
    "ctm_config": {
        "endpoint": "https://beta.carbontransitionmodel.com/api/",
        "CTM_scenario_ID": "base",
        "ETM_scenario_ID": "13579"
    },
    "base_path": "meso",
    "input_esdl_file_path": "input_file.esdl",
    "output_esdl_file_path": "output_file.esdl"
}

res = requests.post(api_endpoint + '/model/initialize/' + model_run_id, json=post_body)
if res.ok:
    print("Endpoint /model/initialize ok!")
    result = res.json()
    print(result)
else:
    print("Endpoint /model/initialize not ok!")
    exit(1)

res = requests.get(api_endpoint + '/model/run/' + model_run_id)
if res.ok:
    print("Endpoint /model/run ok!")
    result = res.json()
    print(result)
else:
    print("Endpoint /model/run not ok!")
    exit(1)

res = requests.get(api_endpoint + '/model/status/' + model_run_id)
if res.ok:
    print("Endpoint /model/status ok!")
    result = res.json()
    print(result)
else:
    print("Endpoint /model/status not ok!")
    exit(1)

res = requests.get(api_endpoint + '/model/results/' + model_run_id)
if res.ok:
    print("Endpoint /model/results ok!")
    result = res.json()
    print(result)
else:
    print("Endpoint /model/results not ok!")
    exit(1)

res = requests.get(api_endpoint + '/model/remove/' + model_run_id)
if res.ok:
    print("Endpoint /model/remove ok!")
    result = res.json()
    print(result)
else:
    print("Endpoint /model/remove not ok!")
    exit(1)
