from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRegister, UserLogin
from app.services.user_service import register_user, get_all_users, login_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
def register(user: UserRegister):
    return register_user(user)


@router.post("/login")
def login(user: UserLogin):
    return login_user(user)


@router.get("/all")
def get_users():
    return {"users": get_all_users()}


@router.put("/{user_id}")
def update_user(user_id: str, user: UserRegister):
    return update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: str):
    return delete_user(user_id)


