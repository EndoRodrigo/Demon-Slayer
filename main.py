from fastapi import FastAPI
from enum import Enum

app = FastAPI()

pilares = [
    {
		"id": 1,
		"name": "Giyu Tomioka",
		"habilidades": ["Aqua Sword", "Water Breathing"],
		"range": "Novato",
        "edad": 23,
        "altura": 1.78,
        "estado": True
	},
    {
		"id": 2,
		"name": "Sakonji Urokodaki",
		"habilidades": ["Aqua Sword", "Water Breathing"],
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