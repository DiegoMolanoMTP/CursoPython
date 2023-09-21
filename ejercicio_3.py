import requests
import json
def test(a,b):
    url = "https://faas-fra1-afec6ce7.doserverless.co/api/v1/web/fn-1f1056ff-de8e-4509-9811-27a68419f504/default/add"
    payload = {"a": a, "b": b}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=payload)

    if 'result' not in json.loads(response.text):
        raise Exception("No hay result")

    return int(json.loads(response.text)['result']) == 4

assert test(1,3) == 4