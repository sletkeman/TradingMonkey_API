"""
defines history routes
"""
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Query, Response, status
from pydantic import BaseModel, typing
from app.services.etrade import (
    get_auth_url,
    get_auth_session,
    renew_session,
    fetch_accounts,
    fetch_portfolio
)
from app.services.db import (
    get_user_etrade_params,
    save_auth_request,
    save_session,
)

USER_ID = 62 # scott's id

router = APIRouter()

class AuthResponse(BaseModel):
    authUrl: str
    authenticated: bool

@router.get("/auth",
            response_model=AuthResponse,
            description="gets the auth response",
            summary="Gets the auth response"
            )
def get_auth():
    "gets the auth url"
    try:
        params = get_user_etrade_params(USER_ID)
        today = datetime.now()
        dt = params.get('CreateDateTime')
        authorized = False
        if not params.get('ConsumerKey') or not params.get('ConsumerSecret'):
            raise HTTPException(status_code=500, detail="Users need an ETrade consumer key and secret before they can use this service.")

        if dt and dt.day == today.day and dt.month == today.month and dt.year == today.year:
            authorized = renew_session(params['ConsumerKey'], params['ConsumerSecret'], params['AccessToken'], params['AccessSecret'])
            if authorized:
                return { 'authUrl': '', 'authenticated': True }
        if not authorized:
            url, token, secret = get_auth_url(params['ConsumerKey'], params['ConsumerSecret'])
            save_auth_request(token, secret, USER_ID)
            return { 'authUrl': url, 'authenticated': False }
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
        access_token, access_token_secret = get_auth_session(params['RequestToken'], params['RequestSecret'], code, params['ConsumerKey'], params['ConsumerSecret'])
        save_session(access_token, access_token_secret, USER_ID)
        return Response(status_code=status.HTTP_204_NO_CONTENT) 
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

class Account(BaseModel):
    accountId: str
    accountIdKey: str
    accountMode: str
    accountDesc: str
    accountName: str
    accountType: str
    institutionType: str
    accountStatus: str
    closedDate: datetime = None

@router.get("/accounts",
            response_model=List[Account],
            description="gets the user's accounts",
            summary="Gets the user's accounts"
            )
def get_accounts():
    "gets a user's etrade accounts"
    try:
        params = get_user_etrade_params(USER_ID)
        return fetch_accounts(params['ConsumerKey'], params['ConsumerSecret'], params['AccessToken'], params['AccessSecret'])
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


@router.get("/portfolio",
            response_model=typing.Any,
            description="gets the user's account portfolio",
            summary="Gets the user's account portfolio"
            )
def get_portfolio(account_id: str):
    "gets a user's etrade account portfolio"
    try:
        params = get_user_etrade_params(USER_ID)
        result = fetch_portfolio(account_id, params['ConsumerKey'], params['ConsumerSecret'], params['AccessToken'], params['AccessSecret'])
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
