"""
a place to include routers
"""

from fastapi import APIRouter
from app.routers import (
    history,
    etrade,
    monkey
)

router = APIRouter()

router.include_router(history.router, prefix="/history", tags=['History'])
router.include_router(etrade.router, prefix="/etrade", tags=['ETrade'])
router.include_router(monkey.router, prefix="/monkey", tags=['Monkey'])

