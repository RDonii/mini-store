from fastapi import APIRouter

from app.api.endpoints import login, users, categories, product_types, product

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, tags=["users"], prefix='/users')
api_router.include_router(categories.router, tags=["categories"], prefix='/categories')
api_router.include_router(product_types.router, tags=["product-types"], prefix='/product-types')
api_router.include_router(product.router, tags=["products"], prefix='/products')