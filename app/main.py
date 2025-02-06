from fastapi import FastAPI
from app.routes.user_route import router as user_router

app = FastAPI()

app.include_router(user_router)

