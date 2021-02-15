"""
defines history routes
"""
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Query, Response, status
from pydantic import BaseModel
from app.services.etrade import (
    get_auth_url,
    get_auth_session
)
from app.services.db import (
    get_user_etrade_params,
    save_auth_request,
    save_session
)

USER_ID = 57 # scott's id

router = APIRouter()

class AuthUrl(BaseModel):
    url: str

@router.get("/auth",
            response_model=AuthUrl,
            description="gets the auth url",
            summary="Gets the auth url"
            )
def get_auth():
    "gets the auth url"
    try:
        params = get_user_etrade_params(USER_ID)
        url, token, secret = get_auth_url()
        save_auth_request(token, secret, USER_ID)
        return { 'url': url }
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

@router.post("/session",
            description="creates the session",
            summary="creates the session",
            responses={204: {"model": None}},
            )
def post_auth_session(code: str):
    "gets the access token"
    try:
        params = get_user_etrade_params(USER_ID)
        session = get_auth_session(params['RequestToken'], params['RequestSecret'], code)
        save_session(session.access_token, session.access_token_secret, USER_ID)
        return Response(status_code=status.HTTP_204_NO_CONTENT) 
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))