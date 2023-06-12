from sqlalchemy.orm import Session
from models.user import User as UserModel
from schemas.user import User as UserSchema

def get_user(db: Session, user_id: int):
    return db.query(UserSchema).filter(UserSchema.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserSchema).filter(UserSchema.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserSchema).offset(skip).limit(limit).all()


def create_users(db: Session, user: UserModel):
    db_user = UserSchema(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()
