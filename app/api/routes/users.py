# routes/users.py
from fastapi import APIRouter
from app.api.controllers.usersCtrl import get_users

router = APIRouter()

@router.get("/users")
def users():
    return get_users()
