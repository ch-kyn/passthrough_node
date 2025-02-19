from fastapi import FastAPI, Request
import requests

def passthrough_node_get(request: Request, path_parameter: str):
    host = request.client.host
    data_source_id = path_parameter

    get_url = f'http://{host}/{data_source_id}'
    get_response = requests.get(get_url)

    if get_response.status_code == 200:
        print(get_response.content.decode('utf-8'))