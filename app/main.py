from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import googleSheets

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(googleSheets.router)
