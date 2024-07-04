from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from lib.user import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from helpers.response_helpers import (
    ErrorResponseModel,
    ResponseModel,
)

from models.user import (
    UpdateUserModel,
    UserModel,
)

router = APIRouter()

@router.post("/user", response_description="User data added into the database")
async def addUser(user: UserModel = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")

@router.get("/user",  response_description="users retrieved")
async def getAllUSers():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

@router.get("/user/{user_id}")
async def getUSer(user_id: str):
    user = await retrieve_user(user_id)
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")

@router.put("/user/{user_id}")
async def updateUser(user_id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_user_data = await update_user(user_id, req)
    if update_user_data:
        return ResponseModel(
            "User with ID: {} name update is successful".format(user_id),
            "User details updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.delete("/user/{user_id}", response_description="User data deleted from the database")
async def deleteUser(user_id: str):
    deleted_user = await delete_user(user_id)
    if deleted_user:
        return ResponseModel(
            "User with ID: {} removed".format(user_id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(user_id)
    )