from pydantic import BaseModel, Field

class BlogCreate(BaseModel):
    name: str = Field(..., description="enter your name")
    description: str = Field(..., description="enter your description")

class Blog(BlogCreate):
    id: int

    class Config:
        from_attributes = True