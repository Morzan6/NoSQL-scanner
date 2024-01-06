from tools.db import Database
from pydantic import BaseModel, Field
from fastapi import HTTPException, status, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, Any


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
