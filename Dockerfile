# 1. 使用官方 Python 3.11 slim 映像
FROM python:3.11-slim

# 2. 設定工作目錄
WORKDIR /app

# 3. 複製 requirements.txt 並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 複製程式碼
COPY ./app ./app

# 5. 對外開放 8000 port
EXPOSE 8000

# 6. 啟動 FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
