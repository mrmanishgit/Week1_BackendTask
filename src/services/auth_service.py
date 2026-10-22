
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.repositories.user_repository import (
    create_user,
    get_by_email,
    get_by_username,
)
from src.schemas.user_schema import UserCreate
from src.security.jwt import (
    create_access_token,
    hash_password,
    verify_password,
)


def register_user(db: Session, data: UserCreate):
    if get_by_username(db, data.username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists",
        )

    if get_by_email(db, str(data.email)):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    try:
        return create_user(
            db=db,
            username=data.username,
            email=str(data.email),
            hashed_password=hash_password(data.password),
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already exists",
        )


def login_user(db: Session, username: str, password: str):
    user = get_by_username(db, username)

    if (
        user is None
        or not user.is_active
        or not verify_password(password, user.hashed_password)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer",
    }
