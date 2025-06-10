from fastapi import FastAPI
from app.routers.routes import router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Car API")
# Configure allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],  # Change this to match your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
