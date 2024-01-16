import sqlite3
from typing import Any


class Database:
    """
    Database api class
    """

    def __init__(self):
        self.connect = sqlite3.connect("db/database.db", check_same_thread=False)
        self.cursor = self.connect.cursor()

        if not self.check_table("Users") or not self.check_table("Scans"):
            self.create_tables()

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    def commit(self):
        self.connect.commit()

    def close(self):
        self.connect.close()
        self.cursor.close()

    def execute(self, query: str, *args) -> int | None:
        self.cursor.execute(query, *args)
        return self.cursor.lastrowid

    def check_table(self, table_name: str) -> Any:
        query: str = f"""SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"""
        self.execute(query)
        return self.cursor.fetchone()

    def create_tables(self) -> None:
        """
        Create tables
        """
        users: str = """
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NULL,
                    password TEXT NOT NULL
                ); 
                """
        scans: str = """
                CREATE TABLE IF NOT EXISTS Scans (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT NOT NULL,
                    description TEXT,
                    type TEXT NULL,
                    status TEXT NOT NULL,
                    version TEXT NULL,
                    ip TEXT NOT NULL,
                    port INTEGER NOT NULL,
                    vuln_data TEXT,
                    datetime TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES Users (id)
                );"""
        self.execute(users)
        self.execute(scans)
