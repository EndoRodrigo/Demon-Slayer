
from pydantic import BaseModel

class Pilar(BaseModel):
    id: int 
    name: str
    range: str 
    edad: int 
    altura: float 
    status: bool 

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Giyu Tomioka",
                "range": "Novato",
                "edad": 23,
                "altura": 1.78,
                "status": False
            }
        }

