from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRegister, UserLogin
from app.services.user_service import register_user, get_all_users

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
def register(user: UserRegister):
    return register_user(user)


@router.get("/all")
def get_users():
    return {"users": get_all_users()}
