from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_ALCHEMY_URL = "sqlite:///./blog.db"

engine = create_engine(SQL_DATABASE_ALCHEMY_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=True)

Base = declarative_base()