from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

app = FastAPI()

# CORS 允許前端連線
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue 所在網址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 假資料的登入帳密
#USER = {"username": "admin", "password": "password"}

#@app.post("/login")
#def login(form: dict):
#    if form["username"] == USER["username"] and form["password"] == USER["password"]:
#        return {"message": "Login success!"}
#    raise HTTPException(status_code=401, detail="Login failed")

@app.get("/excel")
#def get_excel_data():
#    try:
#        df = pd.read_excel("/home/ben/bdm-chat/BDM-US.xlsx")  # 你自己的 Excel 檔名
#        data = df.to_dict(orient="records")
#        return data
#    except Exception as e:
#        raise HTTPException(status_code=500, detail=str(e))
def get_excel_data():
    df = pd.read_excel("/home/ben/bdm-chat/BDM-US.xlsx")  # 替換成你放的 Excel 檔案
    df = df.replace([np.nan, np.inf, -np.inf], None)  # 避免 JSON 格式錯誤
    return df.to_dict(orient="records")
