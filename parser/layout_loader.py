import json
import os

SCHEMA_DIR = "./schemas"

def load_layout(source_system, layout_key, version="1.0"):
    filename = f"{source_system}_{layout_key}_v{version}.json"
    path = os.path.join(SCHEMA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Layout not found: {filename}")
    with open(path, "r") as f:
        return json.load(f)
