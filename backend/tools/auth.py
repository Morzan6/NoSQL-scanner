import hashlib
from tools.db import Database
from pydantic import BaseModel, Field
from fastapi import HTTPException, status, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import time
from typing import Dict, Any
from config import JWT_SECRET, JWT_ALGORITHM

class User:
    """Object to handle communication with user in database"""    
    
    def __init__(self, username: str):
        self.db: Database = Database()
        self.username: str = username
        self.id: int | None = None
        self.is_exist: bool = False
        
        query: str = f"""SELECT * FROM Users WHERE username='{self.username}'"""
        self.db.execute(query)
        user: tuple = self.db.cursor.fetchone()
        
        if user:
            self.is_exist = True
            self.id, self.username, _ = user

    def create(self, password: str) -> None:
        """Creates user in database, 

        Args:
            password (str): user password
        """        
        hashed_password: str = hashlib.sha256(password.encode()).hexdigest()

        query: str = f"""INSERT INTO Users (username, password) VALUES (?,?)"""
        values = (self.username, hashed_password)
        self.id = self.db.execute(query, values)
        self.db.commit()
        self.is_exist = True

    def check_password(self, password: str) -> bool:
        """Checks if user password in database equal given password

        Args:
            password (str): given user password

        Returns:
            bool
        """        
        hashed_password: str = hashlib.sha256(password.encode()).hexdigest()
        query: str = f"""SELECT password FROM Users WHERE username='{self.username}'"""
        self.db.execute(query)
        db_password = self.db.cursor.fetchone()
        print(db_password, hashed_password)
        if db_password == (hashed_password,):
            return True
        return False
    
    def __repr__(self) -> str | None:
        return repr([self.id, self.username])


class Token():
    """Object to handle JWT token"""

    def generate_token(username: str) -> str:
        """Generate JWT token with given username
        Args:
            username (str): user's username

        Returns:
            str: JWT access token
        """
        payload: dict = {
            "username": username,
            "expires": time.time() + 86400
        }
        print(payload)
        token: str = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return token

    def decode_token(token: str) -> dict:
        """Decodes JWT token or raises exceptions if some error occured

        Args:
            token (str): user JWT token

        Raises:
            HTTPException: Token expired
            HTTPException: Invalid Credentials

        Returns:
            dict: token payload
        """
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
    """Object to check user permission on visit route. 
    On __call__ object checks if user's JWT token from Request correct and raises exceptions if it doesn't
    
    Returns:
        str: username from correct JWT token"""
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str | None:
        """Checks if user authentificated, returns username if he does, overwise returns exceptions

        Args:
            request (Request)

        Raises:
            HTTPException: Invalid authentication scheme.
            HTTPException: Invalid token or expired token.
            HTTPException: Invalid authorization code.

        Returns:
            str | None: username
        """
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            isValid, payload = self.verify_jwt(credentials.credentials)
            if not isValid:
                raise HTTPException(
                    status_code=403, detail="Invalid or expired token.")

            return payload.get('username')
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> tuple[bool, dict | None]:
        """Checks if JWT token correct 

        Args:
            jwtoken (str): User JWT token

        Returns:
            tuple[bool, dict | None]: (isTokenValid, payload)
        """
        isTokenValid: bool = False

        try:
            payload = Token.decode_token(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid, payload

JWT_PERMISSION = Depends(JWTBearer())