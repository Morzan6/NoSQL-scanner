from fastapi import APIRouter, Depends, HTTPException, status, Response
from pydantic import BaseModel

ENDPOINT = "auth"

ROUTER = APIRouter(prefix=f"/api/{ENDPOINT}", tags=[ENDPOINT])

class UserLogin(BaseModel):
    username: str
    password:  str

@ROUTER.get("/", status_code=201)
def main():
    return {"": "AUTH"}


@ROUTER.post("/create", status_code=status.HTTP_201_CREATED)
def main(data: UserLogin) -> dict:
    
    return data
