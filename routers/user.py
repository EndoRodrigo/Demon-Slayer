from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from services.user import *
from models.user import User as UserModel
from schemas.user import User
from db.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

#app = FastAPI()
user_router = APIRouter()



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.post("/users/", response_model=UserModel)
def create_user(user: UserModel, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_users(db,user)


@user_router.get("/users/", response_model=list[UserModel])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/users/{user_id}", response_model=UserModel)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.get("/user_by_email/", response_model=UserModel)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db,email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user