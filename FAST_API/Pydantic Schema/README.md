# Pydantic Schema Guide

Pydantic is a data validation and settings management library for Python that uses Python type annotations. It is widely used with FastAPI to define request and response models.

## Defining a Pydantic Schema
A Pydantic schema (also called a model) is created by defining a class that inherits from `pydantic.BaseModel`.

### Example:
```python
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field
```

## Field Validation
Pydantic allows setting constraints on fields.

### Example:
```python
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)
```

## Using Schemas in FastAPI
FastAPI automatically converts request and response bodies to and from Pydantic models.

### Example:
```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users/")
async def create_user(user: UserSchema):
    return {"message": "User created", "user": user}
```

## Nested Models
Pydantic allows nesting models inside each other.

### Example:
```python
from typing import List

class AddressSchema(BaseModel):
    street: str
    city: str
    country: str

class UserWithAddressSchema(BaseModel):
    name: str
    email: str
    addresses: List[AddressSchema]
```

## Data Serialization
Pydantic models can be easily converted to dictionaries or JSON.

### Example:
```python
user = UserSchema(id=1, name="John Doe", email="john@example.com", age=30)
print(user.dict())  # Convert to dictionary
print(user.json())  # Convert to JSON
```

## ORM Mode
Pydantic can work with ORMs like SQLAlchemy by enabling `orm_mode`.

### Example:
```python
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
```

## Custom Validators
You can define custom validation methods using `@validator`.

### Example:
```python
from pydantic import BaseModel, validator

class UserSchema(BaseModel):
    name: str
    email: str

    @validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email address")
        return v
```

## Default Values and Aliases
Pydantic allows setting default values and field aliases.

### Example:
```python
class ConfigSchema(BaseModel):
    debug: bool = False
    database_url: str = Field(..., alias="DATABASE_URL")
```
### Example:
```ptrhon
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AddressSchema(BaseModel):
    street: str
    city: str
    country: str

class UserWithAddressSchema(BaseModel):
    name: str
    email: str
    addresses: List[AddressSchema]

@app.post("/users/")
async def create_user(user: UserWithAddressSchema):
    return {"message": "User created", "user": user}
    
```
#### When to Use Pydantic Schema?

| HTTP Method | Request Body Allowed? | Use Pydantic Schema? |
|------------|----------------------|----------------------|
| POST       | ✅ Yes                | ✅ Yes (for request body validation) |
| PUT        | ✅ Yes                | ✅ Yes (for updating data) |
| PATCH      | ✅ Yes                | ✅ Yes (for partial updates) |
| DELETE     | ❌ No (typically)     | ❌ No (use path params instead) |
| GET        | ❌ No                 | ❌ No (use query/path params) |



## Conclusion
Pydantic makes data validation and serialization simple and efficient. It is an essential tool for FastAPI applications, ensuring structured and type-safe data handling.

