# Python Polymorphism

## Definition
Polymorphism in Python means "many forms" and refers to the ability of an object to take on different forms. It allows functions, methods, or objects to process differently based on their types or class.

---

## Key Principles of Polymorphism
1. **Polymorphic Functions or Methods**: Functions can operate on different types of objects without knowing their exact class.
2. **Method Overloading (Limited in Python)**: Using a method name for different types of data but distinguished by arguments.
3. **Method Overriding**: When a derived class provides its own version of a method already defined in its base class.
4. **Duck Typing**: If an object looks like a duck and quacks like a duck, it is treated as a duck. In Python, as long as an object has the expected method or attribute, it works for the operation.

---

## Examples

### 1. Polymorphic Function or Method
```python
def add(x, y):
    return x + y

# Add numbers
print(add(3, 4))  # Output: 7

# Add strings
print(add("Hello", "World"))  # Output: HelloWorld

# Add lists
print(add([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]
```
Here, the function `add` adapts its behavior based on the types of `x` and `y`.

---

### 2. Method Overriding
```python
class Shape:
    def area(self):
        return "Area of shape undefined."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Using the polymorphic behavior
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(shape.area())
```
**Output:**
```
78.5
24
```
Each object (`Circle` and `Rectangle`) calls its own version of the `area` method.

---

### 3. Duck Typing
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())
```
**Output:**
```
Woof!
Meow!
Moo!
```
Here, even though `Dog`, `Cat`, and `Cow` are not related by inheritance, Python invokes the appropriate `speak` method for each instance based on the concept of duck typing.

---

### 4. Simulating Method Overloading
```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(3, 4))        # Output: 7
print(calc.add(3, 4, 5))     # Output: 12
```
Python uses variable-length arguments (`*args`) to mimic method overloading behavior.

---

## Benefits of Polymorphism
1. **Code Reusability**: A single function or method works for different objects or types.
2. **Improved Readability**: Simplifies extending the behavior for new objects or classes.
3. **Flexibility**: Easy to add functionality with less modification to existing code.

---

## Applications of Polymorphism
1. **Interface Implementation**: A base interface defines the structure, and derived classes provide specific functionality.
2. **Dynamic Method Selection**: Behavior of a class can be changed dynamically at runtime.
3. **Framework Development**: Enhances reusable frameworks by allowing classes with varying behaviors to be used interchangeably.
