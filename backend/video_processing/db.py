from pymongo import MongoClient
from datetime import datetime

# Replace with your own Mongo URI
client = MongoClient("mongodb://LanTech:L%40nc%5Eere%400012@192.168.48.201:27017/SuperDB?authSource=admin")  # or use Atlas URI

db = client["ai_interview_db"]
collection = db["transcripts"]

def save_to_mongodb(data: dict):
    data["timestamp"] = datetime.utcnow()
    collection.insert_one(data)
