import sqlite3
from typing import Any

class Database:
    """
    Database api class
    """

    def __init__(self):
        self.connect = sqlite3.connect("database.db")
        self.cursor = self.connect.cursor()
        
        if not self.check_table('Users') or not self.check_table('Scans'):
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
                    user INTEGER, 
                    type TEXT NULL,
                    status TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    datetime TEXT NOT NULL,
                    FOREIGN KEY (user) REFERENCES Users (id)
                );"""
        self.execute(users)
        self.execute(scans)



# db = Database()
# print(db.check_table("Scans"))
