from pymongo import MongoClient
from fastapi import HTTPException

client = MongoClient("mongodb://localhost:27017")
db = client["layout_db"]
layouts_collection = db["layouts"]

def normalize_version(version: str) -> str:
    # Normalize version like "1.0" -> "1"
    return version.split(".")[0]

def load_layout(source_system: str, layout_key: str, version: str = "1"):
    version = normalize_version(version)

    query = {
        "source_system": source_system,
        "layout_key": layout_key,
        "version": version
    }

    doc = layouts_collection.find_one(query)

    if not doc:
        raise HTTPException(
            status_code=404,
            detail=f"Layout not found for {source_system} {layout_key} v{version}"
        )

    return doc.get("fields", [])
