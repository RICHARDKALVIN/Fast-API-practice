import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

mongoDbUrl =os.getenv("MONGODB_URL")
mongoDataBase = os.getenv("DB_NAME")

client = AsyncIOMotorClient(mongoDbUrl)

db = client[mongoDataBase]



def get_database():
    return db

