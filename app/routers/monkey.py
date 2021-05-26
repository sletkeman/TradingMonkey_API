"""
defines history routes
"""
from datetime import datetime, date
from typing import List
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, typing
from app.services.db import (
    get_users,
    get_monkey_positions,
    get_user_monkeys
)

router = APIRouter()

@router.get("/users",
            response_model=typing.Any,
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
            response_model=typing.Any,
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

@router.get("/positions",
            response_model=typing.Any,
            description="gets the monkey's positions",
            summary="gets the monkey's positions"
            )
def get_positions(monkeyId: int, currentDate: date):
    "gets the monkey's positions"
    try:
        result = get_monkey_positions(monkeyId, currentDate)
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))