from fastapi import FastAPI
import datetime
from pydantic import BaseModel
import databases
import sqlalchemy

app=FastAPI()

class User(BaseModel):
    username: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class Poll(BaseModel):

    title:str
    type_poll: str
    is_add_choices_active: bool
    is_voting_active: bool
    created_by: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def root():
    return {"user":"hello"}

@app.post("/users/")
async def create_user(user: User):
    return user


@app.post("/polls/")
async def create_user(poll: Poll):
    return poll
