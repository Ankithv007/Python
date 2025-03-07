from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import Schemas, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog/", response_model=Schemas.Blog)
async def create_blog(blog: Schemas.BlogCreate, db: Session = Depends(get_db)):
    db_blog = models.Blog(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog