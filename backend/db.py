from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://loksai2024:<db_password>@cluster0.5hn4myx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGO_URI)

db = client["user_auth_db"]  #  DB name
users_collection = db["users"]  # collection name
