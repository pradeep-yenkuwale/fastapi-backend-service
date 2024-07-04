import motor.motor_asyncio

MONGO_URI = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

database = client.users

user_collection = database.get_collection("users")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "phone_number": user["phone_number"]
    }

def get_user_collection():
    return user_collection