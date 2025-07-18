from config.database import get_user_collection, user_helper
from bson.objectid import ObjectId
from fastapi import HTTPException
from helpers.user_helpers import get_hashed_password, verify_password

user_collection = get_user_collection()

# Retrieve all users present in the database


async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user_password = user_data['password']
    hashed_password = get_hashed_password(user_password)
    user_data.update({"password": hashed_password})
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    print("id", id)
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
    else:
        raise HTTPException(status_code=404, detail="User not found!")


# Retrieve a user with a matching email
async def get_user_by_email(email: str, send_password=None) -> dict:
    user = await user_collection.find_one({"email": email})
    if user:
        return user_helper(user, send_password)
    else:
        raise HTTPException(status_code=404, detail="User not found!")