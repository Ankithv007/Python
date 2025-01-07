# Method Overloading in Python

## What is Method Overloading?
Method overloading allows a class to have multiple methods with the same name but different parameters. It is used to perform different operations based on the number or type of arguments passed.

However, **Python does not support method overloading** directly, as the latest definition of a method overrides the previous ones in the same class. Python achieves method overloading behavior using default arguments, variable-length arguments, or external libraries like `singledispatch`.

---

## Simulating Method Overloading in Python

### Using Default Arguments
Default arguments allow a single method to behave differently based on the arguments passed.

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example
calc = Calculator()
print(calc.add(5))        # Output: 5 (Only 'a' is considered)
print(calc.add(5, 3))     # Output: 8 (a + b)
print(calc.add(5, 3, 2))  # Output: 10 (a + b + c)
```

---

### Using Variable-Length Arguments (`*args` and `**kwargs`)
With `*args`, you can handle any number of positional arguments. Similarly, `**kwargs` allows for keyword arguments.

```python
class Calculator:
    def add(self, *args):
        return sum(args)

# Example
calc = Calculator()
print(calc.add(2, 3))           # Output: 5
print(calc.add(2, 3, 4))        # Output: 9
print(calc.add(1, 2, 3, 4, 5))  # Output: 15
```

---

### Using the `@singledispatch` Decorator
The `functools.singledispatch` decorator allows you to define a generic function and create multiple specialized versions of it based on the input type.

```python
from functools import singledispatch

@singledispatch
def process(data):
    raise NotImplementedError("Unsupported type")

@process.register
def _(data: int):
    return f"Processing integer: {data}"

@process.register
def _(data: str):
    return f"Processing string: {data}"

# Example
print(process(10))        # Output: Processing integer: 10
print(process("Hello"))   # Output: Processing string: Hello
```

---

## Limitations of Method Overloading in Python
1. **Latest Definition Wins**: If you define two methods with the same name, the last definition overwrites the previous ones.
   ```python
   class Test:
       def greet(self):
           print("Hello!")

       def greet(self, name):
           print(f"Hello, {name}!")

   obj = Test()
   obj.greet("Ankith")  # Output: Hello, Ankith!
   ```

2. **Workarounds Required**: Since Python does not directly support method overloading, workarounds such as `*args`, `**kwargs`, or `singledispatch` are necessary.

---

## Comparison with Other Languages
Unlike Java or C++ where multiple methods with the same name can coexist with different parameter lists, Python uses a single method definition that adapts dynamically based on arguments.

---

## When to Use Method Overloading
- When implementing functionality that varies based on the number or type of parameters.
- For cleaner and more flexible method handling (especially with `singledispatch`).

---

## Example: Combining Techniques
A class demonstrating overloaded-like behavior based on different approaches:

```python
from functools import singledispatch

class Greeter:
    def greet(self, *args):
        if len(args) == 0:
            return "Hello!"
        elif len(args) == 1:
            return f"Hello, {args[0]}!"
        else:
            return f"Hello, {' and '.join(args)}!"

# Generic greet using singledispatch
@singledispatch
def specialized_greet(data):
    return "Hello, guest!"

@specialized_greet.register
def _(data: str):
    return f"Hello, {data}!"

@specialized_greet.register
def _(data: list):
    return f"Hello, {', '.join(data)}!"

# Example
greeter = Greeter()
print(greeter.greet())              # Output: Hello!
print(greeter.greet("Ankith"))      # Output: Hello, Ankith!
print(greeter.greet("Ankith", "B V"))  # Output: Hello, Ankith and B V!

print(specialized_greet("Ankith"))     # Output: Hello, Ankith!
print(specialized_greet(["A", "B"]))   # Output: Hello, A, B!
