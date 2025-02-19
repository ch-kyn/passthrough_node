from fastapi import FastAPI, Request
import requests

app = FastAPI()

MAIN_NODE_URL = "https://cloud-lab5.onrender.com"

@app.get("/{full_path:path}")
def passthrough_node_get(full_path: str):
    get_url = f"{MAIN_NODE_URL}/{full_path}"
    cache = {}

    try:
        if full_path not in cache:
            response = requests.get(get_url)

            # add cache here I guess
            cache[full_path] = response.json()
            return response.json()
        else:
            return cache[full_path]
        
    except requests.exceptions.RequestException as e:
        return {"error": "Failed to fetch data", "details": str(e)}
        
    
