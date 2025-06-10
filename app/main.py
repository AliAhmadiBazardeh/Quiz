from fastapi import FastAPI
from app.routers.routes import router

app = FastAPI(title="Car API")

app.include_router(router)
