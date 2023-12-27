import os
DESCRIPTION = "Rest API Implementation to scan NoSQL Databases"
VERSION = "0.1"
ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
]

JWT_SECRET = os.getenv('JWT_SECRET', '1234')
JWT_ALGORITHM = "HS256"