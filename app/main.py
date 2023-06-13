import asyncio
from fastapi import FastAPI
from app.routers import router

from app.utils.update_costs import UpdatePrices


app = FastAPI()

app.include_router(router=router)

task = asyncio.create_task(UpdatePrices().update())