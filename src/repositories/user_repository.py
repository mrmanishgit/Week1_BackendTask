
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User


def get_by_username(db: Session, username: str):
    return db.scalar(select(User).where(User.username == username))


def get_by_email(db: Session, email: str):
    return db.scalar(select(User).where(User.email == email))


def get_by_id(db: Session, user_id: int):
    return db.get(User, user_id)


def create_user(db: Session, username: str, email: str, hashed_password: str):
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
