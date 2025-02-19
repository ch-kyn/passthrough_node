from fastapi import FastAPI, Request
import requests

app = FastAPI()

MAIN_NODE_URL = "https://cloud-lab5.onrender.com"

@app.get("/{full_path:path}")
def passthrough_node_get(full_path: str):
    get_url = f"{MAIN_NODE_URL}/{full_path}"
    try:
        response = requests.get(get_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch data", "details": str(e)}
    
    # add cache here
    
