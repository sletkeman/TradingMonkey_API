"""
defines history routes
"""
from datetime import datetime, date
from typing import List
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from pydantic.typing import Any, List
from decimal import Decimal
from app.services.db import (
    get_users,
    get_monkey_positions,
    get_user_monkeys
)

router = APIRouter()

@router.get("/users",
            response_model=Any,
            description="gets the users",
            summary="Gets the users"
            )
def get_usrs():
    "gets a user's monkeys"
    try:
        result = get_users()
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

@router.get("/monkeys",
            response_model=Any,
            description="gets the user's monkeys",
            summary="Gets the user's monkeys"
            )
def get_monkeys(userId):
    "gets a user's monkeys"
    try:
        result = get_user_monkeys(userId)
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

class Position(BaseModel):
    Symbol: str
    Shares: int
    OpenDate: date
    OpenPrice: Decimal
    isShort: bool
    CurrentDate: date
    CurrentPrice: Decimal

@router.get("/positions",
            response_model=List[Position],
            description="gets the monkey's positions",
            summary="gets the monkey's positions"
            )
def get_positions(monkeyId: int):
    "gets the monkey's positions"
    try:
        result = get_monkey_positions(monkeyId)
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))