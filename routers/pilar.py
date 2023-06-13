
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine, Base
from models.pilar import Pilar
from services.pilar import get_pilares, create_pilares, update_pilares

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


pilar_router = APIRouter()

@pilar_router.get("/getpilares", tags=['Pilares principales'], response_model=dict())
def get_pillares(db: Session = Depends(get_db)) -> dict():
    lista = get_pilares(db)
    return lista

@pilar_router.post("/CreatePilar", tags=['Pilares principales'], response_model=dict())
def create_pilar(pilar: Pilar, db: Session = Depends(get_db)) -> dict():
    return create_pilares(db, pilar)

@pilar_router.put("/updatepilar", tags=['Pilares principales'])
def update_pilar(pilar: Pilar,db: Session = Depends(get_db)):
    return update_pilares(db,pilar)
