# FastAPI Application

## Overview
This is a FastAPI application with a structured project layout. It includes database integration using SQLAlchemy, schema validation with Pydantic, and CRUD operations.

## Project Structure
```
fastapi_app/
│── main.py          # Entry point for the FastAPI application
│── database.py      # Database connection setup
│── models.py        # SQLAlchemy database models
│── schemas.py       # Pydantic schemas for data validation
│── crud.py          # CRUD operations
│── requirements.txt # List of dependencies
│── .env             # Environment variables
```

## Setup Instructions

### 1. Install Dependencies
```sh
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
Create a `.env` file and define the database connection string:
```
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
```

### 3. Database Configuration
#### `database.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 4. Define Models
#### `models.py`
```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
```

### 5. Define Schemas
#### `schemas.py`
```python
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True
```

### 6. CRUD Operations
#### `crud.py`
```python
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()
```

### 7. Main Application
#### `main.py`
```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
import crud, schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
```

### 8. Initialize the Database
```sh
python -c 'from database import Base, engine; Base.metadata.create_all(bind=engine)'
```

### 9. Run the FastAPI Application
```sh
uvicorn main:app --reload
```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/users/` | Get all users |
| POST | `/users/` | Create a new user |

## Contributing
Feel free to submit issues and pull requests for improvements!

## License
This project is licensed under the MIT License.

