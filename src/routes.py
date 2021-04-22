from fastapi import APIRouter

from src.controller import property_info

api_router = APIRouter()
api_router.include_router(property_info.router, tags=["property_info"])