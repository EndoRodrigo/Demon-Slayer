from fastapi import FastAPI, Query
from enum import Enum
from typing import Union, Annotated
from pydantic import BaseModel

app = FastAPI()

class Pilar(BaseModel):
    id: int 
    name: str
    skill: list
    range: str | None = None
    edad: int | None = None
    altura: float | None = None
    status: bool | None = None 


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


@app.get("/")
def get_pillares():
    return pilares


@app.get("/pilar/{id}")
def get_pilar(id: int):
    for find_pilar in pilares:
        if id == find_pilar.get('id'):
            return find_pilar
    return []



@app.get("/pilar/rango/{range}")
def get_pillar_by_rango(range: SelectRange):
    for find_pilar in pilares:
        if range == find_pilar.get('range'):
            return find_pilar

    return []

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

@app.post("/create/")
def create_pilar(pilar: Pilar):
    pilares.append(pilar)
    return pilares

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results