from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .databases import create


app = FastAPI()

@app.post("/id/{id}")
async def createid(id:int):
    await create(id)
    return {"id":id}

