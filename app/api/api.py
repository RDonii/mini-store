from fastapi import APIRouter

from app.api.endpoints import login, users, categories

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, tags=["users"], prefix='/users')
api_router.include_router(categories.router, tags=["categories-products"], prefix='/categories')
