from fastapi import FastAPI
from app.car.api import routes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.handlers.exception_handlers import global_exception_handler

app = FastAPI(title="Car API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(routes.router)

app.add_exception_handler(Exception, global_exception_handler)
