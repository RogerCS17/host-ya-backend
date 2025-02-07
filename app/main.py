from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import user_route, space_route, comment_route, rating_route
app = FastAPI()

app.include_router(user_route.router)
app.include_router(space_route.router)
app.include_router(comment_route.router)
app.include_router(rating_route.router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")