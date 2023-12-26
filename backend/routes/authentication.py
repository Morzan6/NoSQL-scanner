from fastapi import APIRouter, Depends, HTTPException, status, Response
from tools.auth import User, Token, JWT_PERMISSION
from typing import Annotated, Dict

ENDPOINT = "auth"

ROUTER = APIRouter(prefix=f"/api/{ENDPOINT}", tags=[ENDPOINT])

@ROUTER.get("/", status_code=200, dependencies=[JWT_PERMISSION])
def main(username:  Annotated[str, JWT_PERMISSION]) -> dict:
    print(username)
    return {"": "AUTH"}


@ROUTER.post("/create", status_code=status.HTTP_201_CREATED)
def create(data: User.UserLoginSerializer) -> dict:
    """Route for user creation in DB with given username and password.

    Args:
        data (dict): {"username": "yourusername","password": "yourpassword"}

    Raises:
        HTTPException: User with this username already exists

    Returns:
        dict: {"status": "User successfully added"}
    """
    user: User = User(data.username)
    if user.exist():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists",
        )
    user.create(data.password)
    print(data)
    return {"status": "User successfully added"}


@ROUTER.post("/login", 
             status_code=status.HTTP_200_OK, 
             response_model=Token.TokenSerializer)
def login(data: User.UserLoginSerializer) -> dict:
    """Route for user login with given username and password. Endpoint returns JWT access token.

    Args:
        data (dict): {"username": "yourusername","password": "yourpassword"}

    Raises:
        HTTPException: User does not exist
        HTTPException: Wrong password

    Returns:
        dict: {"access_token": "somejwttoken"}
    """

    user: User = User(data.username)

    if not user.exist():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist",
        )
    if not user.check_password(data.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong password",
        )
    return {"access_token": Token.generate_token(data.username)}
