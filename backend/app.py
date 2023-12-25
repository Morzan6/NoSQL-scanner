from fastapi import FastAPI
import uvicorn
import routes as RT
from fastapi.middleware.cors import CORSMiddleware

DESCRIPTION = "Rest API Implementation to scan NoSQL Databases"
VERSION = "0.1"

ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI(
    title="NoSQL-Scanner API",
    description=DESCRIPTION,
    version=VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RT.AUTH)
app.include_router(RT.SCAN)

if __name__ == "__main__":
    uvicorn.run(app)
