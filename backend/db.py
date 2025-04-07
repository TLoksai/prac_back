from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017/"
client = AsyncIOMotorClient(MONGO_URI)

db = client["user_auth_db"]  #  DB name
users_collection = db["users"]  # collection name
