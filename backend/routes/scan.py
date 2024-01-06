from fastapi import APIRouter, Depends, HTTPException, status, Response
from tools.auth import User, Token, JWT_PERMISSION
from tools.scanning import Scan
from typing import Dict, Annotated, Any, List
from serializers import ScanStartSerializer

ENDPOINT = "scan"

ROUTER = APIRouter(prefix=f"/api/{ENDPOINT}", tags=[ENDPOINT])


@ROUTER.post("/start", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def start(user: Annotated[User, JWT_PERMISSION], data: ScanStartSerializer) -> Dict[str, int]:
    print(user, data)
    scan_id: int = 0
    return {"scan_id": scan_id}


@ROUTER.get("/status", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def scan_status(user: Annotated[User, JWT_PERMISSION], id: int) -> Dict[str, str]:
    scan: Scan = Scan(id)
    if scan.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can not access another user's scan",
        )

    return {"status": scan.status}


@ROUTER.get("/", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def scan(user: Annotated[User, JWT_PERMISSION], id: int) -> Dict[str, str | int]:
    print(user.scans)
    scan = Scan(id)
    if scan.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can not access another user's scan",
        )

    return {
        "id": scan.id,
        "type": scan.type,
        "ip": scan.ip,
        "port": scan.port,
        "datetime": scan.datetime,
        "vulnerability_data": scan.vuln_data,
    }


@ROUTER.get("/my", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def scan(user: Annotated[User, JWT_PERMISSION]) -> List[Dict[str, int | str]]:
    response = []
    for scan_id in user.scans:
        scan = Scan(scan_id)
        response.append(
            {"id": scan.id, "status": scan.status, "type": scan.datetime, "ip": scan.ip}
        )

    return response
