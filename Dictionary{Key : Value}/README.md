# Python Dictionary  

## Overview  
A **dictionary** in Python is an unordered, mutable collection that stores data in **key-value pairs**. It allows fast access, insertion, and deletion of elements based on keys.  

## Key Features  
- **Key-Value Pairs**: Each item is stored as a pair of a unique key and its corresponding value.  
- **Mutable**: The contents can be changed after creation.  
- **Unordered**: Before Python 3.7, dictionaries were unordered. From Python 3.7 onwards, they maintain insertion order.  
- **Fast Lookups**: Retrieval of values by keys is efficient.  

## Syntax  
```python
# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with data
my_dict = {
    "name": "John",
    "age": 30,
    "is_employed": True
}
---
#  Accessing Values
my_dict = {"name": "Alice", "age": 25}

# Access a value by key
print(my_dict["name"])  # Output: Alice

# Use `get()` to avoid KeyError
print(my_dict.get("city", "Not Found"))  # Output: Not Found

---
# Adding or Updating Items

my_dict = {"name": "Bob"}
my_dict["age"] = 32  # Add a new key-value pair
my_dict["name"] = "Robert"  # Update an existing value

--- 
# Removing Items
my_dict = {"name": "Tom", "age": 40}

# Remove a specific key-value pair
my_dict.pop("age")

# Remove and return the last key-value pair (Python 3.7+)
my_dict.popitem()

# Clear the dictionary
my_dict.clear()

---
# Iterating Through a Dictionary
my_dict = {"name": "Eva", "age": 28}

# Iterate through keys
for key in my_dict:
    print(key)

# Iterate through values
for value in my_dict.values():
    print(value)

# Iterate through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

---
# Nested Dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

print(nested_dict["person1"]["name"])  # Output: Alice

---
# Dictionary Comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

---
```

``` 
# Python Dictionary Methods

## Overview
Python dictionaries come with several built-in methods that simplify various operations, such as accessing, updating, and managing key-value pairs.

---

## Dictionary Methods

| **Method**         | **Description**                                          |
|---------------------|----------------------------------------------------------|
| `get(key, default)` | Returns the value for a key, or a default value if the key is not found. |
| `keys()`            | Returns a view object containing all the keys in the dictionary. |
| `values()`          | Returns a view object containing all the values in the dictionary. |
| `items()`           | Returns a view object containing all key-value pairs in the dictionary. |
| `update(other)`     | Merges another dictionary into the current dictionary. Existing keys are updated. |
| `pop(key)`          | Removes the specified key and returns its value. Raises a `KeyError` if the key is not found. |
| `popitem()`         | Removes and returns the last key-value pair as a tuple. (Insertion order preserved in Python 3.7+.) |
| `clear()`           | Removes all items from the dictionary, leaving it empty. |
| `copy()`            | Returns a shallow copy of the dictionary.               |

---

## Examples

### Using `get()` Method
```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("city", "Not Found"))  # Output: Not Found

```
```python
# Using keys() and values()
my_dict = {"name": "Eva", "age": 28}
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Eva
# age: 28

---
# Using items() Method
my_dict = {"name": "Eva", "age": 28}
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Eva
# age: 28

---
# Using update()
my_dict = {"name": "Tom"}
my_dict.update({"age": 40, "city": "New York"})
print(my_dict)  # Output: {'name': 'Tom', 'age': 40, 'city': 'New York'}

---
# Using pop() and popitem()
my_dict = {"name": "Alice", "age": 25}
print(my_dict.pop("age"))  # Output: 25
print(my_dict.popitem())   # Output: ('name', 'Alice')

---
# Using clear() and copy()
my_dict = {"name": "Bob"}
copied_dict = my_dict.copy()
my_dict.clear()
print(my_dict)       # Output: {}
print(copied_dict)   # Output: {'name': 'Bob'}

---
```




