from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(..., description="enter your title")
    body: str = Field(..., description="enter your body description")


    