from fastapi import FastAPI, Request
import requests

app = FastAPI()

MAIN_NODE_URL = "https://cloud-lab5.onrender.com"  # Your actual main node URL

@app.get("/{path_parameter}")
def passthrough_node_get(path_parameter: str):
    get_url = f"{MAIN_NODE_URL}/{path_parameter}"
    try:
        response = requests.get(get_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch data", "details": str(e)}