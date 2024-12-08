from fastapi import APIRouter, Body
from fastapi import Depends
from typing import Annotated

from app.auth.auth_handler import sing_jwt
from app.hasher.hash_handler import encode_data
from app.model import UserLoginSchema, UserSchema

router = APIRouter(
    prefix='/user',
)

users = []


def check_user(data: UserLoginSchema) -> bool:
    for user in users:
        if user.email == data.email and user.password == encode_data(data.password):
            return True
    return False


@router.get("", tags=["user"])
async def get_users() -> dict:
    return {
        "data": users
    }

@router.post("/singup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    password = user.password
    user.password = encode_data(password)
    users.append(user)
    return sing_jwt(user.email)


@router.post("/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sing_jwt(user.email)
    return {
        "error": "Wrong login or password!"
    }