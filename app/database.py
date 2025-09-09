from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 資料庫 URL（檔案會存到 cloudops-todo/todo.db）
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

# 建立資料庫引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 每個請求會用到的 SessionLocal（跟 DB 的連線）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 宣告模型基底
Base = declarative_base()