from fastapi import APIRouter, Depends, HTTPException, status, Response
from tools.auth import User, Token, JWT_PERMISSION

ENDPOINT = "scan"

ROUTER = APIRouter(prefix=f"/api/{ENDPOINT}", tags=[ENDPOINT])


@ROUTER.get("/", status_code=201)
def main():
    return {"": "SCAN"}
