import os
import json
from pymongo import MongoClient

# === CONFIG ===
SCHEMA_DIR = "schemas"  # Directory containing layout JSON files
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "layout_db"
COLLECTION_NAME = "layouts"


def parse_filename(filename):
    """
    Expected format: <source_system>_<layout_key>_v<version>.json
    Example: DBAR_DEMOGRAPHIC_v1.json
    """
    
    parts = filename.replace(".json", "").split("_")
    if len(parts) != 3 or not parts[2].startswith("v"):
        raise ValueError(
            f"Filename '{filename}' is not in expected format: <System>_<LayoutKey>_v<version>.json"
        )

    source_system = parts[0]
    layout_key = parts[1]
    version = parts[2].replace("v", "")
    return source_system, layout_key, version


def load_layouts_to_mongo():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    for filename in os.listdir(SCHEMA_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(SCHEMA_DIR, filename)

            try:
                source_system, layout_key, version = parse_filename(filename)
            except ValueError as e:
                print(f"Skipping '{filename}': {e}")
                continue

            with open(filepath, "r") as file:
                data = json.load(file)

            # Flatten layout if needed
            layout_fields = data.get("fields", [])
            if isinstance(data.get("fields"), dict) and "fields" in data["fields"]:
                layout_fields = data["fields"]["fields"]

            doc = {
                "source_system": source_system,
                "layout_key": layout_key,
                "version": str(version),
                "fields": layout_fields
            }

            # Upsert into Mongo
            result = collection.update_one(
                {
                    "source_system": source_system,
                    "layout_key": layout_key,
                    "version": str(version)
                },
                {"$set": doc},
                upsert=True
            )

            print(f"Loaded: {filename} -> upserted: {result.upserted_id}")

    print("✔ All layouts loaded into MongoDB.")


if __name__ == "__main__":
    load_layouts_to_mongo()
