from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the MongoDB client and database
client = MongoClient(os.getenv("MONGO_URI"))

db_obj = client["voice_assistant"]
