"""
Api entry point.
"""

from fastapi import FastAPI
from api.controllers.balances_controller import BALANCES_ROUTER
from api.controllers.event_controller import EVENT_ROUTER

app = FastAPI()
app.include_router(BALANCES_ROUTER)
app.include_router(EVENT_ROUTER)

if __name__ == "__main__":
    print("Usage: uvicorn main:app [add --reload dev code]")
