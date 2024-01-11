import hashlib
from tools.db import Database
from pydantic import BaseModel, Field
from fastapi import HTTPException, status, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import datetime
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
    """Object to handle communication with scan in database"""

    def __init__(self, scan_id: int | None = None) -> None:
        self.db: Database = Database()

        self.id: int = scan_id
        self.type: str | None = None
        self.status: str | None = None
        self.version: str | None = None
        self.user_id: int | None = None
        self.ip: str | None = None
        self.port: int | None = None
        self.vuln_data: str | None = None
        self.datetime: str | None = None
        self.name: str | None = None
        self.description: str | None = None

        if not scan_id:
            return

        self.db.execute(
            f"""SELECT type, user_id, status, version, ip, port, vuln_data, datetime, name, description 
                FROM Scans WHERE id='{self.id}'"""
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
            self.version,
            self.ip,
            self.port,
            self.vuln_data,
            self.datetime,
            self.name,
            self.description,
        ) = scan

    def new(
        self,
        user_id: int,
        ip: str,
        port: int,
        name: str,
        description: str = "My scan",
        type: str = None,
        status: str = "STARTED",
        version: str = None,
        vuln_data: str = None,
    ):
        """Creates new scan in Database and returns self objec with given propperties

        Args:
            user_id (int): user's id
            ip (str): ip
            port (int): port
            name (str): name of scan
            type (str, optional): service type: 'redis', 'mongodb' etc.
            status (str, optional): scan status. Defaults to "STARTED".
            version (str, optional): version of scanned service. Defaults to None.
            vuln_data (str, optional): parsed vulnerabillity data . Defaults to None.
        """
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values: tuple = (user_id, type, status, version, ip, port, dt, vuln_data, name, description)

        query: str = f"""INSERT INTO Scans (user_id, type, status, version, ip, port, datetime, vuln_data, name, description) 
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

        self.db.execute(query, values)
        self.db.commit()
        self.id = self.db.cursor.lastrowid
        self.type = type
        self.status = status
        self.version = version
        self.user_id = user_id
        self.ip = ip
        self.port = port
        self.vuln_data = vuln_data
        self.datetime = dt
        self.name = name
        self.description = description

        return self

    def save(self) -> None:
        """Saves scan object in database

        Returns:
            int: last row id of updated scan in database.
        """
        query: str = f"""UPDATE Scans
                        SET type='{self.type}', 
                        status='{self.status}', 
                        version='{self.version}', 
                        ip='{self.ip}', 
                        port='{self.port}', 
                        datetime='{self.datetime}', 
                        vuln_data='{self.vuln_data}',
                        name='{self.name}'
                        WHERE id='{self.id}';"""
        self.db.execute(query)
        self.db.commit()

        return self.db.cursor.lastrowid

    def __repr__(self) -> str:
        return f"Scan({str([self.id, self.type, self.user_id, self.status, self.version, self.ip, self.port, self.vuln_data, self.datetime])})"
