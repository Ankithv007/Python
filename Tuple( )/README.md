# Python Tuples

## Introduction

A **tuple** is an immutable sequence in Python, commonly used to group related data. Unlike lists, tuples cannot be modified after their creation, making them useful for storing constant data.

---

## Key Characteristics of Tuples

1. **Ordered**: Elements in a tuple maintain their order.
2. **Immutable**: Tuples cannot be modified after creation.
3. **Heterogeneous**: Can contain elements of different data types.
4. **Allows Duplicates**: Tuples can include duplicate values.

---

## Creating a Tuple

Tuples are created using parentheses `()` or the `tuple()` constructor.

```python
# Examples of tuple creation
empty_tuple = ()                 # An empty tuple
single_item = (1,)               # Tuple with one item (note the comma)
numbers = (1, 2, 3)              # Tuple with integers
mixed_tuple = (1, "Hello", 3.5)  # Mixed data types
nested_tuple = ((1, 2), (3, 4))  # Nested tuples

# Using tuple() constructor
constructed_tuple = tuple([1, 2, 3])

```python
# Indexing
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])  # Output: 10 (First element)
print(my_tuple[-1]) # Output: 40 (Last element)

# Slicing
print(my_tuple[1:3]) # Output: (20, 30) (From index 1 to 2)

---
# Unpacking a Tuple
# Assigning tuple values to variables
point = (10, 20)
x, y = point
print(x)  # Output: 10
print(y)  # Output: 20

---
# Accessing elements in nested tuples
nested = ((1, 2), (3, 4))
print(nested[1][0]) # Output: 3




