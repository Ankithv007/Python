# FastAPI Path Parameters

## Introduction
FastAPI provides an efficient way to handle path parameters in API endpoints. Path parameters are part of the URL and are used to pass dynamic values to API routes.

## Defining Path Parameters
Path parameters in FastAPI can be defined using curly braces `{}` inside the route path.

### Basic Path Parameters
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```
**Example Request:**
```
GET /items/42
```
**Response:**
```json
{
  "item_id": 42
}
```

## Path Parameters with String Type
```python
@app.get("/users/{username}")
def get_user(username: str):
    return {"username": username}
```
**Example Request:**
```
GET /users/johndoe
```
**Response:**
```json
{
  "username": "johndoe"
}
```

## Path Parameters with Validation
FastAPI allows constraints on path parameters using `Path` from `fastapi`.

```python
from fastapi import Path

@app.get("/products/{product_id}")
def get_product(product_id: int = Path(..., title="Product ID", ge=1, le=1000)):
    return {"product_id": product_id}
```
### Explanation:
- `...` (Ellipsis) makes the parameter mandatory.
- `ge=1` ensures the value is greater than or equal to 1.
- `le=1000` ensures the value is less than or equal to 1000.

## Multiple Path Parameters
```python
@app.get("/orders/{order_id}/items/{item_id}")
def get_order_item(order_id: int, item_id: int):
    return {"order_id": order_id, "item_id": item_id}
```
**Example Request:**
```
GET /orders/10/items/5
```
**Response:**
```json
{
  "order_id": 10,
  "item_id": 5
}
```

## Combining Path and Query Parameters
Path parameters can be used alongside query parameters:
```python
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int, active: bool = True):
    return {"customer_id": customer_id, "active": active}
```
**Example Request:**
```
GET /customers/123?active=false
```
**Response:**
```json
{
  "customer_id": 123,
  "active": false
}
```

## Conclusion
Path parameters in FastAPI provide a flexible way to handle dynamic data in API requests. Using `Path`, you can add validation and metadata to improve API reliability.
