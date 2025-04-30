# BDM Chat 專案

## 專案介紹
這是一個使用Vue 3和FastAPI的Excel數據展示應用，包含登入功能。

## 技術棧
- 前端：Vue 3 + Vite
- 後端：FastAPI (Python)
- 容器化：Docker + Docker Compose

## 開始使用

### 前提條件
- Docker
- Docker Compose

### 安裝步驟
1. 克隆倉庫
```bash
git clone https://github.com/[你的用戶名]/bdm-chat.git
cd bdm-chat
```

2. 啟動應用
```bash
docker-compose up --build
```

3. 訪問應用
- 前端：`http://localhost:5173`
- 後端API：`http://localhost:8000`

### 登入
- 帳號：admin
- 密碼：password

## 目錄結構
- `backend/`: FastAPI 後端
- `frontend/`: Vue 前端
- `docker-compose.yml`: Docker Compose 配置
