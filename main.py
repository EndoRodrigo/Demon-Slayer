from fastapi import FastAPI, Query
from enum import Enum
from typing import Union, Annotated, List
from pydantic import BaseModel
from routers.user import user_router


app = FastAPI()
app.include_router(user_router)

class Pilar(BaseModel):
    id: int 
    name: str
    skill: list = []
    range: str | None = None
    edad: int | None = None
    altura: float | None = None
    status: bool | None = None 

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Giyu Tomioka",
                "skills": ["Aqua Sword", "Water Breathing"],
                "range": "Novato",
                "edad": 23,
                "altura": 1.78,
                "estado": False
            }
        }


pilares = [
    {
		"id": 1,
		"name": "Giyu Tomioka",
		"skills": ["Aqua Sword", "Water Breathing"],
		"range": "Novato",
        "edad": 23,
        "altura": 1.78,
        "estado": True
	},
    {
		"id": 2,
		"name": "Sakonji Urokodaki",
		"skills": ["Aqua Sword", "Water Breathing"],
		"range": "Pilar",
        "edad": 58,
        "altura": 1.68,
        "estado": False
	}

]

class SelectRange(str, Enum):
    pilar = "Pilar"
    intermedio = "Intermedio"
    novato = "Novato"


@app.get("/", tags=['Pilares principales'], response_model=dict())
def get_pillares() -> dict():
    return pilares


@app.get("/pilar/{id}", tags=['Pilares principales'], response_model=dict())
def get_pilar(id: int) -> dict():
    for find_pilar in pilares:
        if id == find_pilar.get('id'):
            return find_pilar
    return []



@app.get("/pilar/rango/{range}", tags=['Pilares principales'])
def get_pillar_by_rango(range: SelectRange):
    for find_pilar in pilares:
        if range == find_pilar.get('range'):
            return find_pilar

    return []

@app.post("/create/", tags=['Pilares principales'], response_model=Pilar)
def create_pilar(pilar: Pilar):
    pilares.append(pilar)
    return pilares[-1]

@app.get("/items/", tags=['Pilares principales'])
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results