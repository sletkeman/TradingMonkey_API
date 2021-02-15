"""
defines history routes
"""
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from services.etrade import (
    get_auth_url,
    get_auth_session
)

router = APIRouter()

class AuthUrl(BaseModel):
    url: str
    secret: str

@router.get("/url",
            response_model=AuthUrl,
            description="gets the auth url",
            summary="Gets the auth url"
            )
def get_auth_url():
    "gets the auth url"
    try:
        url, secret = get_auth_url()
        return {
            'url': url,
            'secret': secret
        }
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

class Session(BaseModel):
    token: str
    secret: int

@router.get("/session",
            response_model=Session,
            description="gets the access token",
            summary="Gets the access token"
            )
def get_auth_session(token: str, secret: str, code: str):
    "gets the access token"
    try:
        session = get_auth_session(token, secret, code)
        return {
            'token': session['oauth_token'],
            'secret': session['oauth_token_secret'],
        }
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))