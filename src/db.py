from pymongo import MongoClient

# Initialize the MongoDB client and database
client = MongoClient("mongodb://localhost:27017")

db_obj = client["voice_assistant"]
