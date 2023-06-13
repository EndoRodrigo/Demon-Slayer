from fastapi import FastAPI
from routers.user import user_router
from routers.pilar import pilar_router


app = FastAPI()
app.include_router(user_router)
app.include_router(pilar_router)




