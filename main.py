from fastapi import FastAPI, Query
from enum import Enum
from typing import Union, Annotated, List
from pydantic import BaseModel
from routers.user import user_router
from routers.pilar import pilar_router


app = FastAPI()
app.include_router(user_router)
app.include_router(pilar_router)




