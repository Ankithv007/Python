# FastAPI Query Parameters

## Introduction
Query parameters in **FastAPI** allow us to pass data in the URL while making requests. They are part of the **query string**, which comes after the `?` symbol in the URL.

## How Query Parameters Work
Query parameters are automatically detected when function parameters are not part of the path.

### Example:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = None):
    return {"query": q}

GET http://127.0.0.1:8000/items/?q=fastapi

```

### Example 2 :
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return{"welcome Home"}

#http://127.0.0.1:8000/

@app.get("/name")
def read_name(name:str):
    return{"your name is:":name}
# # http://127.0.0.1:8000/name?name=ankith

@app.get("/about")
def read_name(name:str,age:int,sex:str):
    return{
        "my name is":name,
        "my age is": age,
        "my sex is": sex
    }
# http://127.0.0.1:8000/about?name=ankith&age=24&sex=male

```

# Query Parameters with Type Validation
- FastAPI automatically validates query parameter types.
```python
@app.get("/products/")
async def get_products(price: float, available: bool):
    return {"price": price, "available": available}

#GET http://127.0.0.1:8000/products/?price=199.99&available=true
```
 
# Optional and Default Values
- You can define optional query parameters using Optional from typing and set default values.
```python
from typing import Optional

@app.get("/users/")
async def get_user(name: Optional[str] = "Guest"):
    return {"user": name}

# GET http://127.0.0.1:8000/users/
```

# Required Query Parameters
- If a query parameter has no default value, it is required.
```python
@app.get("/profile/")
async def get_profile(username: str):  # No default value -> required
    return {"username": username}

# GET http://127.0.0.1:8000/profile/
```

# Summary
1.Query parameters are included after ? in the URL.
2.Parameters with default values are optional, otherwise they are required.
3.FastAPI automatically validates parameter types.
4.Multiple query parameters can be used together.
5.If a parameter is None, it is not included in the response.

Feature | /about (Query Parameters) | /user/{user_id}/item/{item_id}/class/{class_id} (Path Parameters)
--------|---------------------------|------------------------------------------------
Parameter Type | Query parameters | Path parameters
Example URL | /about?name=John&age=30&sex=male | /user/10/item/42/class/5
Where Parameters are Passed? | In the ?name=value format in the URL | Directly inside the URL path
Mandatory? | Can be optional (default values can be set) | Always required
Used For | Filtering, optional values, search queries | Identifying specific resources like user IDs, item IDs

