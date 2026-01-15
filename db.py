import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  

MONGO_HOST = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
MONGO_USERNAME = os.environ.get("MONGO_USERNAME","admin")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_AUTH_SOURCE = os.environ.get("MONGO_AUTH_SOURCE")

client = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource=MONGO_AUTH_SOURCE)

db = client[MONGO_DB]
collection = db["top_threats"]
