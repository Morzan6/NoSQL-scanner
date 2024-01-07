import hashlib
from tools.db import Database
from pydantic import BaseModel, Field
from fastapi import HTTPException, status, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import time
from typing import Dict, Any, List
from config import JWT_SECRET, JWT_ALGORITHM


class User:
    """Object to handle communication with user in database"""

    def __init__(self, username: str):
        self.db: Database = Database()
        self.username: str = username
        self.id: int | None = None
        self.is_exist: bool = False

        query: str = (
            f"""SELECT id, username FROM Users WHERE username='{self.username}'"""
        )
        self.db.execute(query)
        user: tuple = self.db.cursor.fetchone()

        if user:
            self.is_exist = True
            self.id, self.username = user
            self.scans: List[int] = self.get_scans()

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

    def get_scans(self) -> List[int]:
        """Get all users scans

        Returns:
            List[int]: list of user's scans ids
        """
        self.db.execute(f"""SELECT id FROM Scans WHERE user_id='{self.id}'""")
        return [i for (i,) in self.db.cursor.fetchall()]

    def __repr__(self) -> str | None:
        return f"User({str([self.id, self.username])})"



class Scan:
    def __init__(self, scan_id: int) -> None:
        self.db: Database = Database()

        self.id: int = scan_id
        self.type: str
        self.user_id: int
        self.ip: str
        self.port: int
        self.vuln_data: str
        self.datetime: str

        self.db.execute(
            f"""SELECT type, user_id, status, ip, port, vuln_data, datetime FROM Scans WHERE id='{self.id}'"""
        )

        scan: tuple = self.db.cursor.fetchone()

        if not scan:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Invalid scan id"
            )
        (
            self.type,
            self.user_id,
            self.status,
            self.ip,
            self.port,
            self.vuln_data,
            self.datetime,
        ) = scan

    def __repr__(self) -> str | None:
        return f"Scan({str([self.id, self.type, self.user_id, self.status, self.ip, self.port, self.vuln_data, self.datetime])})"
