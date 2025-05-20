from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["layout_db"]
layouts_collection = db["layouts"]
