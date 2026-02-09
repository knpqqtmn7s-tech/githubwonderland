from fastapi import APIRouter, status
from schemas.user_schema import UserCreate
from controllers.user_controller import get_users, create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", status_code=status.HTTP_200_OK)
def list_users():
    return get_users()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: UserCreate):
    return create_user(user)
