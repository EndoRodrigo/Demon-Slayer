from sqlalchemy import Boolean, Column, Float, Integer, String
from db.database import Base


class Pilar(Base):

    __tablename__ = "pilares"
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    range= Column(String)
    edad= Column(Integer)
    altura= Column(Float)
    status= Column(Boolean)
