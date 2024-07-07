import motor.motor_asyncio

MONGO_URI = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

database = client.users

user_collection = database.get_collection("users")


def user_helper(user, send_password=None) -> dict:
    user_dict = {
        "id": str(user["_id"]),
        "name": user["name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "phone_number": user["phone_number"],
    }
    if send_password is True:  user_dict["password"] = user["password"]
    return user_dict


def get_user_collection():
    return user_collection
