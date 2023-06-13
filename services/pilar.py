from sqlalchemy.orm import Session
from schemas.pilar import Pilar as PilarSchema
from models.pilar import Pilar as PilarModel

def get_pilares(db: Session):
    return db.query(PilarSchema).all()

def get_pilar(db: Session, user_id: int):
    return db.query(PilarSchema).filter(PilarSchema.id == user_id).first()


def get_pilar_by_rango(db: Session, email: str):
    return db.query(PilarSchema).filter(PilarSchema.email == email).first()


def get_pilar_by_maximo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PilarSchema).offset(skip).limit(limit).all()

def create_pilares(db: Session, user: PilarModel):
    db_user = PilarSchema(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
