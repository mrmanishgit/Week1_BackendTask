
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.schemas.user_schema import UserCreate, UserResponse, TokenResponse
from src.security.jwt import get_current_user
from src.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, data)


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return login_user(db, form_data.username, form_data.password)


@router.get("/me", response_model=UserResponse)
def read_current_user(user=Depends(get_current_user)):
    return user
