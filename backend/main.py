from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

app = FastAPI()

# CORS 允許前端連線
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

from pydantic import BaseModel
from fastapi import HTTPException

class LoginRequest(BaseModel):
    username: str
    password: str

# 預設帳號密碼
DEFAULT_USER = {
    "username": "admin",
    "password": "password"
}

@app.post("/login")
def login(request: LoginRequest):
    if (request.username == DEFAULT_USER["username"] and 
        request.password == DEFAULT_USER["password"]):
        return {"message": "Login successful", "status": "success"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/excel")
def get_excel_data():
    df = pd.read_excel("/app/BDM-US.xlsx")  # Docker 容器內路徑
    df = df.replace([np.nan, np.inf, -np.inf], None)  # 避免 JSON 格式錯誤
    return df.to_dict(orient="records")
