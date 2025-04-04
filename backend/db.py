from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)

db = client["user_auth_db"]  # Your DB name
users_collection = db["users"]  # Your collection name
