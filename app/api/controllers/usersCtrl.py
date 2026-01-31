from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate

def get_users(db: Session):
    return db.query(User).all()

def create_user(user_in: UserCreate, db: Session):
    if db.query(User).filter(
        (User.username == user_in.username) |
        (User.email == user_in.email)
    ).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    user = User(
        username=user_in.username,
        email=user_in.email,
        password=user_in.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
