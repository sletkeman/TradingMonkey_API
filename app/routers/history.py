"""
defines history routes
"""
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from services.iex import get_historical

router = APIRouter()

class Quote(BaseModel):
    """inherits from BaseModel to define the Quote object"""
    close: float
    high: float
    low: float
    open: float
    symbol: str
    volume: int
    id: str
    key: str
    subkey: str
    date: str
    updated: int
    changeOverTime: float
    marketChangeOverTime: float
    uOpen: float
    uClose: float
    uHigh: float
    uLow: float
    uVolume: int
    fOpen: float
    fClose: float
    fHigh: float
    fLow: float
    fVolume: int
    label: str
    change: float
    changePercent: float


@router.get("/history/{symbol}",
            response_model=List[Quote],
            description="Gets the quotes",
            summary="Gets the quotes"
            )
def get_history(symbol: str, start = Query(None), end = Query(None)):
    "gets the history"
    try:
        s = datetime.strptime(start, '%Y-%m-%d')
        e = datetime.strptime(start, '%Y-%m-%d')
        return get_historical(symbol, s, e)
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

