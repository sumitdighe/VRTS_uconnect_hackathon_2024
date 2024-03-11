from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .databases import create, delay_hit, frequency_hit,volume_hit


app = FastAPI()

@app.get("/frequency")
async def frequency():
    await frequency_hit()
    return {"message":"success"}
@app.post("/id/{id}")
async def createid(id:int):
    await create(id)
    return {"id":id}

@app.get("/delay")
async def delay():
    await delay_hit()
    return {"message":"success"}

@app.get('/volume')
async def volume():
    await volume_hit()
    return {"message":"success"}