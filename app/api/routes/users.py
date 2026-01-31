from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.controllers.usersCtrl import get_users, create_user
from app.core.db import get_db
from app.schemas.user import UserCreate, UserRead

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[UserRead])
def users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/", response_model=UserRead)
def create(user_in: UserCreate, db: Session = Depends(get_db)):
    return create_user(user_in, db)
