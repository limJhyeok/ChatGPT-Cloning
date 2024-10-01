import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import chat_router, user_router, util_router

load_dotenv()
DEV_FRONTEND_URL = os.getenv("DEV_FRONTEND_URL")

origins = [
    DEV_FRONTEND_URL
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(user_router.router)
app.include_router(chat_router.router)
app.include_router(util_router.router)
# @app.get("/")
# def index():
#   return FileResponse("frontend/dist/index.html")
