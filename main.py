from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from typing import List

from UserRouter import router as user_router
from ItemsRouter import router as item_router
app = FastAPI()

app.include_router(user_router)
app.include_router(item_router)


