from fastapi import APIRouter, Depends, HTTPException, status, Response
from tools.auth import User, Token, JWT_PERMISSION
from typing import Dict, Annotated
from serializers import ScanSerializer

ENDPOINT = "scan"

ROUTER = APIRouter(prefix=f"/api/{ENDPOINT}", tags=[ENDPOINT])


@ROUTER.get("/", status_code=201)
def main():
    return {"": "SCAN"}

@ROUTER.post("/start", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def start(username:  Annotated[str, JWT_PERMISSION], data: ScanSerializer) -> Dict[str, int]:
    print(username, data)
    scan_id = ""
    return {"scan_id": scan_id}
