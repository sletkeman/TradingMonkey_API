"""
Entry point for the FastApi application
"""

from os import environ

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

import env
from app.routers import index

app = FastAPI(
    title="Trading Monkey API",
    description="A set of API endpoints for use by the Trading Monkey",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
