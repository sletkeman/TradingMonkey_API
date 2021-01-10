"""
a place to include routers
"""

from fastapi import APIRouter
from app.routers import (
    history
)

router = APIRouter()

router.include_router(history.router, prefix="/history", tags=['History'])

