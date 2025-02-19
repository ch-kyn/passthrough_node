from fastapi import FastAPI
import requests

def passthrough_node_get(request: Request, path_parameter: path_param):
    host = request.client.host
    # data_source_id = path_parameter.id

    get_url = f'http://{host}'
    get_response = request.get(get_url)

    # if inp_post_response .status_code == 200:
    #  print(json.loads(get_response.content.decode('utf-8')))