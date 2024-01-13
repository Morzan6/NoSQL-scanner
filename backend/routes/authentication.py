from fastapi import APIRouter, Depends, HTTPException, status, Response
from tools.auth import Token, JWT_PERMISSION
from tools.ORM import User
from typing import Annotated, Dict
from serializers import UserLoginSerializer, TokenSerializer

ENDPOINT = "auth"

ROUTER = APIRouter(prefix=f"/api/{ENDPOINT}", tags=[ENDPOINT])

@ROUTER.post("/create", status_code=status.HTTP_201_CREATED)
def create(data: UserLoginSerializer) -> Dict[str, str]:
    """Route for user creation in DB with given username and password.

    Args:
        data (dict): {"username": "yourusername","password": "yourpassword"}

    Raises:
        HTTPException: User with this username already exists

    Returns:
        dict: {"status": "User successfully added"}
    """
    user: User = User(data.username)
    
    if user.is_exist:
        print(user.id)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists",
        )
    user.create(data.password)
    print(user)
    return {"status": "User successfully added"}


@ROUTER.post("/login", 
             status_code=status.HTTP_200_OK, 
             response_model=TokenSerializer)
def login(data: UserLoginSerializer) -> Dict[str, str]:
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

    if not user.is_exist:
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
