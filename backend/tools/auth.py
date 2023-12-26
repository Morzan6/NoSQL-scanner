import hashlib
from tools.db import Database
from pydantic import BaseModel, Field
from fastapi import HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import time
from typing import Dict
from config import JWT_SECRET, JWT_ALGORITHM


class User:

    class UserLoginSerializer(BaseModel):
        username: str = Field(pattern=r"[A-Za-z0-9_@!]+", max_length=100)
        password: str = Field(min_length=8)

    def __init__(self, username: str):
        self.db = Database()
        self.username: str = username

    def exist(self) -> bool:
        query: str = f"""SELECT * FROM Users WHERE username='{self.username}'"""
        self.db.execute(query)
        is_exist = self.db.cursor.fetchone()
        if is_exist:
            return True

        return False

    def create(self, password: str) -> None:
        hashed_password: str = hashlib.sha256(password.encode()).hexdigest()

        query: str = f"""INSERT INTO Users (username, password) VALUES (?,?)"""
        values = (self.username, hashed_password)
        self.db.execute(query, values)
        self.db.commit()

    def check_password(self, password: str) -> bool:
        hashed_password: str = hashlib.sha256(password.encode()).hexdigest()
        query: str = f"""SELECT password FROM Users WHERE username='{self.username}'"""
        self.db.execute(query)
        db_password = self.db.cursor.fetchone()
        print(db_password, hashed_password)
        if db_password == (hashed_password,):
            return True
        return False


class Auth():
    class TokenSerializer(BaseModel):
        access_token: str

    def generate_token(username: str) -> Dict[str, str]:
        payload: dict = {
            "username": username,
            "expires": time.time() + 86400
        }
        print(payload)
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return token

    def decode_token(token: str) -> dict:
        try:
            decoded_token: dict = jwt.decode(
                token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if decoded_token["expires"] >= time.time():
                return decoded_token
            else:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Token expired")
        except jwt.DecodeError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            isValid, payload = self.verify_jwt(credentials.credentials)
            if not isValid:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")

            return payload
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> tuple[bool, dict | None]:
        isTokenValid: bool = False

        try:
            payload = Auth.decode_token(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid, payload