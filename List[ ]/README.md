# Python Lists

## Introduction
A **list** in Python is a versatile and widely used data structure that allows storing a collection of items in a single variable. Lists are ordered, mutable (modifiable), and allow duplicate elements.

## Key Characteristics of Lists
1. **Ordered**: The items in a list maintain their order.
2. **Mutable**: Elements in a list can be modified.
3. **Heterogeneous**: A list can contain elements of different data types.
4. **Allows Duplicates**: Lists can include multiple instances of the same value.

---

## Creating a List
Lists can be created using square brackets `[]` or the `list()` constructor.

```python
# Examples of list creation
empty_list = []                # An empty list
numbers = [1, 2, 3, 4, 5]      # List of integers
mixed_list = [1, "Hello", 3.5] # Mixed data types
nested_list = [[1, 2], [3, 4]] # Nested list (list of lists)

# Using list() constructor
constructed_list = list((1, 2, 3))
---

# Accessing Elements
# Indexing
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # Output: 10 (First element)
print(numbers[-1]) # Output: 50 (Last element)

# Slicing
print(numbers[1:4]) # Output: [20, 30, 40] (From index 1 to 3)

--- 
# Modifying Lists
# Lists can be modified using assignment, append, insert, and remove methods.


# Append
numbers.append(60) # Adds 60 at the end

# Insert
numbers.insert(2, 25) # Inserts 25 at index 2

# Remove by value
numbers.remove(20) # Removes the first occurrence of 20

# Remove by index
del numbers[1]     # Removes the element at index 1

# Pop
last_item = numbers.pop() # Removes and returns the last element

## Concatenation and Repetition

# Concatenation
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2 # Output: [1, 2, 3, 4]

# Repetition
repeated = list1 * 2     # Output: [1, 2, 1, 2]
 
# Membership Testing
print(3 in combined)  # Output: True
print(5 not in combined) # Output: True


# Iteration
for item in numbers:
    print(item)

## List Methods

Below is a table of commonly used methods in Python lists:

| **Method**       | **Description**                                                |
|-------------------|----------------------------------------------------------------|
| `append(x)`       | Adds an item to the end of the list.                           |
| `extend(iterable)`| Extends the list with elements from an iterable.               |
| `insert(i, x)`    | Inserts an item at a specified index.                          |
| `remove(x)`       | Removes the first occurrence of a specified value.             |
| `pop([i])`        | Removes and returns the item at the specified index.           |
| `clear()`         | Removes all elements from the list.                            |
| `index(x)`        | Returns the index of the first occurrence of x.                |
| `count(x)`        | Counts the number of occurrences of x.                         |
| `sort()`          | Sorts the list in ascending order.                             |
| `reverse()`       | Reverses the list in place.                                    |
| `copy()`          | Returns a shallow copy of the list.                            |






