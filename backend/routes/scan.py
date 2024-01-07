from fastapi import APIRouter, Depends, HTTPException, status, Response
from tools.ORM import User
from tools.auth import Token, JWT_PERMISSION
from tools.ORM import Scan
from typing import Dict, Annotated, Any, List
from serializers import ScanStartSerializer

ENDPOINT = "scan"

ROUTER = APIRouter(prefix=f"/api/{ENDPOINT}", tags=[ENDPOINT])


@ROUTER.post("/start", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def start(user: Annotated[User, JWT_PERMISSION], data: ScanStartSerializer) -> Dict[str, int]:
    """Route to start scan by ip and port

    Args:
        user (Annotated[User, JWT_PERMISSION]): User access token in headers
        data (ScanStartSerializer): POST data {
                                                "ip": "123.23.123.24",
                                                "port": 1234  
                                                }

    Returns:
        Dict[str, int]: scan id
    """    
    print(user, data)
    scan_id: int = 0
    return {"scan_id": scan_id}


@ROUTER.get("/status", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def scan_status(user: Annotated[User, JWT_PERMISSION], id: int) -> Dict[str, str]:
    """Route to get status of scan by it's id

    Args:
        user (Annotated[User, JWT_PERMISSION]): User access token in headers
        id (int): GET param

    Raises:
        HTTPException: You can not access another user's scan

    Returns:
        Dict[str, str]: {"status": "scanning"}
    """    
    scan: Scan = Scan(id)
    if scan.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can not access another user's scan",
        )

    return {"status": scan.status}


@ROUTER.get("/get", status_code=status.HTTP_200_OK, dependencies=[JWT_PERMISSION])
def scan(user: Annotated[User, JWT_PERMISSION], id: int) -> Dict[str, str | int]:
    """Route to get scan data by it's id

    Args:
        user (Annotated[User, JWT_PERMISSION]): User access token in headers
        id (int): GET param

    Raises:
        HTTPException: You can not access another user's scan

    Returns:
        Dict[str, str | int]: {
                                "id": 1,
                                "type": "redis",
                                "ip": "123.54.12.43",
                                "port": 12454,
                                "datetime": "2022-06-16 16:37:23",
                                "vulnerability_data": {}
                            }
    """    
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
    """Route to get all user's scans
    Args:
        user (Annotated[User, JWT_PERMISSION]): User access token in headers

    Returns:
        List[Dict[str, int | str]]: [
                                        {
                                            "id": 1,
                                            "status": "ok",
                                            "type": "redis",
                                            "ip": "255.255.255.255"
                                        },
                                        {
                                            "id": 2,
                                            "status": "scanning",
                                            "type": "mongodb",
                                            "ip": "145.243.12.45"
                                        }
                                    ]
    """    
    response = []
    for scan_id in user.scans:
        scan = Scan(scan_id)
        response.append(
            {"id": scan.id, "status": scan.status, "type": scan.datetime, "ip": scan.ip}
        )

    return response
