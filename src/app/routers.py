from fastapi import APIRouter
from src.app.auth.api import auth_router

api_router = APIRouter()

api_router.include_router(auth_router, tags=["login"])
