# Python Functions

Functions in Python are reusable blocks of code designed to perform a specific task. They help make code more organized, modular, and maintainable.

## Table of Contents
- [What is a Function?](#what-is-a-function)
- [Function Syntax](#function-syntax)
- [Function Types](#function-types)
  - [1. Built-in Functions](#1-built-in-functions)
  - [2. User-defined Functions](#2-user-defined-functions)
- [Defining a Function](#defining-a-function)
- [Calling a Function](#calling-a-function)
- [Function Parameters](#function-parameters)
- [Default Arguments](#default-arguments)
- [Keyword Arguments](#keyword-arguments)
- [Variable-length Arguments](#variable-length-arguments)
- [Return Statement](#return-statement)
- [Examples](#examples)
- [Best Practices](#best-practices)

---

## What is a Function?
A **function** is a block of code that performs a specific operation. It can take inputs, process them, and return an output.

### Why Use Functions?
- Code Reusability
- Improved Code Readability
- Better Debugging and Maintenance

---

## Function Syntax

```python
def function_name(parameters):
    """
    Function docstring: Explain the function's purpose here.
    """
    # Function body
    return output  # Optional
```

### Components:
- **`def`**: Keyword to define a function.
- **`function_name`**: Name of the function (should be meaningful).
- **`parameters`**: Input values to the function (optional).
- **`return`**: Used to return the output (optional).

---

## Function Types

### 1. Built-in Functions
Python provides several built-in functions, such as:
- `print()`: To display output.
- `len()`: To find the length of an object.
- `input()`: To take input from the user.

### 2. User-defined Functions
Functions created by the user to perform specific tasks.

Example:
```python
def greet(name):
    return f"Hello, {name}!"
```

---

## Defining a Function

### Example:
```python
def add_numbers(a, b):
    """
    This function adds two numbers.
    """
    return a + b
```

---

## Calling a Function
Invoke a function using its name followed by parentheses.

```python
result = add_numbers(5, 10)
print(result)  # Output: 15
```

---

## Function Parameters

Functions can take different types of arguments:
1. **Positional Arguments**: Arguments are passed in order.
   ```python
   def greet(name, age):
       return f"{name} is {age} years old."

   print(greet("Ankith", 25))
   ```

2. **Default Arguments**: Provide default values for parameters.
   ```python
   def greet(name, age=18):
       return f"{name} is {age} years old."

   print(greet("Ankith"))  # Output: Ankith is 18 years old.
   ```

3. **Keyword Arguments**: Arguments passed as key-value pairs.
   ```python
   print(greet(age=20, name="Ankith"))
   ```

4. **Variable-length Arguments**:
   - **`*args`**: For non-keyword arguments.
   - **`**kwargs`**: For keyword arguments.

   Example:
   ```python
   def display(*args, **kwargs):
       print("Args:", args)
       print("Kwargs:", kwargs)

   display(1, 2, name="Ankith", age=25)
   ```

---

## Return Statement

Functions can return values using `return`.
```python
def square(num):
    return num * num

print(square(4))  # Output: 16
```

---

## Examples

### Example 1: Calculate Factorial
```python
def factorial(n):
    """
    Calculate factorial of n recursively.
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Example 2: Fibonacci Sequence
```python
def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    """
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## Best Practices

1. Use meaningful function names.
2. Document your functions using docstrings.
3. Keep functions short and focused on a single task.
4. Use default arguments to handle optional parameters.
5. Avoid using global variables inside functions.

### Example of a Docstring:
```python
def add_numbers(a, b):
    """
    Add two numbers and return the result.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b
```

---

Feel free to contribute or report issues to improve this repository!
