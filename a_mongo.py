from pymongo import MongoClient
from settings import *

# client = MongoClient(MONGODB_URI)
client = MongoClient(
    MONGODB_HOST,
    MONGODB_PORT,
    username=MONGODB_USER,
    password=MONGODB_PASSWORD,
)
