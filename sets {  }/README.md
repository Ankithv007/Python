## Python Sets
A set in Python is a collection that is unordered, mutable, and does not allow duplicate elements. Sets are useful for storing unique items and performing mathematical set operations like union, intersection, and difference.

### Features of Sets
1. Unordered: Items do not have a defined order.
2. Unique Elements: Duplicate elements are not allowed.
3. Mutable: You can add or remove elements.
4. Set Operations: Supports mathematical operations like union, intersection, difference, etc.


- Creating Sets
```python 
# Creating a set
my_set = {1, 2, 3, 4}

# Creating an empty set
empty_set = set()  # Note: {} creates an empty dictionary, not a set.

# From other iterables
set_from_list = set([1, 2, 3, 4])
set_from_string = set("hello")  # {'h', 'e', 'l', 'o'}

# Adding and Removing Elements
my_set.add(5)           # Add a single element
my_set.update([6, 7])   # Add multiple elements
my_set.discard(4)       # Remove an element (no error if not found)
my_set.remove(2)        # Remove an element (raises KeyError if not found)
my_set.clear()          # Remove all elements

# Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

# Union
union = A | B           # {1, 2, 3, 4, 5}

# Intersection
intersection = A & B    # {3}

# Difference
difference = A - B      # {1, 2}

# Symmetric Difference
symmetric_difference = A ^ B  # {1, 2, 4, 5}

# Membership Testing
1 in my_set   # True
10 not in my_set  # True

# Set Comprehensions
squared_set = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# Frozen Sets
Frozen sets are immutable sets. Once created, their elements cannot be changed.
frozen_set = frozenset([1, 2, 3])
# Operations like union, intersection, etc., are supported but not methods like add or remove.





