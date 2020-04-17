from fastapi import APIRouter
from src.app.auth import api as auth_api

api_router = APIRouter()

api_router.include_router(auth_api.router, tags=["login"])
