import os

DESCRIPTION = "Rest API Implementation to scan NoSQL Databases"
VERSION = "0.1"
ORIGINS = [
    "http://localhost",
    "http://localhost:9000",
    "http://127.0.0.1:4000",
    "https://predprof.tawt.fun/"
]

JWT_SECRET = os.environ.pop('JWT_SECRET')
JWT_ALGORITHM = "HS256"
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
