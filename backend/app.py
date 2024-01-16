import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import routes as RT
from tools.db import Database
from config import *

db = Database()

app = FastAPI(
    title="NoSQL-Scanner API",
    description=DESCRIPTION,
    version=VERSION,
    debug=False
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(RT.AUTHENTICATION)
app.include_router(RT.SCAN)

if __name__ == "__main__":
    uvicorn.run(app)
