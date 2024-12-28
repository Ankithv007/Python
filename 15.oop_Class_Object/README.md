# Python Classes and Objects

## Overview
Classes and objects are core concepts in Object-Oriented Programming (OOP). They enable bundling data and functions into reusable modules, enhancing code organization, readability, and reuse.

---

## **What is a Class?**
A **class** is a blueprint or template for creating objects. It defines attributes (properties) and methods (functions) that objects can have.

### **Features of a Class**
1. **Encapsulation**: Bundles data and methods.
2. **Abstraction**: Hides unnecessary implementation details.
3. **Reusability**: Enables code reuse via inheritance.
4. **Modularity**: Structures the code logically.

---

## **What is an Object?**
An **object** is an instance of a class. It represents a specific entity created using a class blueprint, containing:
1. **Attributes**: Store the object’s state.
2. **Methods**: Define the object’s behavior.

### **Creating an Object**
```python
# Syntax to create an object
object_name = ClassName(arguments)
```

---

## **Components of Classes and Objects**

### **Class Syntax**
```python
class ClassName:
    # Class attribute (shared by all objects)
    class_variable = "Shared Value"

    # Constructor method (called on object creation)
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance attribute

    # Instance method (accessed by the object)
    def instance_method(self):
        return f"Instance attribute: {self.instance_variable}"

    # Class method (accessed via the class)
    @classmethod
    def class_method(cls):
        return f"Class variable: {cls.class_variable}"

    # Static method (independent of the object and class)
    @staticmethod
    def static_method():
        return "Static method logic here."
```

### **Attributes**
Attributes store data for the class and objects. There are two main types:

1. **Class Attributes**: Shared by all objects of the class.
2. **Instance Attributes**: Unique to each object.

### **Methods**
Methods define the behavior of a class or object.
1. **Instance Method**: Operates on instance attributes via `self`.
2. **Class Method**: Operates on class attributes using `@classmethod`.
3. **Static Method**: Does not depend on instance/class; uses `@staticmethod`.

---

## **Special Methods (Magic/Dunder Methods)**
These methods provide additional functionality and begin/end with double underscores.

| Method   | Description                            |
|----------|----------------------------------------|
| `__init__` | Constructor, initializes an object.    |
| `__str__`  | Converts an object to a string.       |
| `__repr__` | Returns a developer-friendly string. |
| `__len__`  | Called with `len()`.                 |

### Example:
```python
class Special:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Special Object with name {self.name}"

obj = Special("Python")
print(obj)  # Output: Special Object with name Python
```

---

## **Principles of OOP**

1. **Encapsulation**: Bundling data and methods together.
   ```python
   class EncapsulationExample:
       def __init__(self):
           self._protected = "Protected attribute"

       def get_protected(self):
           return self._protected

   obj = EncapsulationExample()
   print(obj.get_protected())
   ```

2. **Inheritance**: Enables code reuse by deriving new classes from existing ones.
   ```python
   class Parent:
       def greet(self):
           print("Hello from Parent!")

   class Child(Parent):
       pass  # Inherits the greet method from Parent

   obj = Child()
   obj.greet()  # Output: Hello from Parent!
   ```

3. **Polymorphism**: Allows different objects to respond differently to the same method call.
   ```python
   class Parent:
       def introduce(self):
           print("I am the parent")

   class Child(Parent):
       def introduce(self):
           print("I am the child")

   obj = Child()
   obj.introduce()  # Output: I am the child
   ```

4. **Abstraction**: Hides internal details using abstract classes and methods.

---

## **Access Modifiers**
Control the accessibility of attributes and methods.
1. **Public**: Accessible anywhere.
2. **Protected**: Prefix with `_`; meant for internal use.
3. **Private**: Prefix with `__`; restricts access.

### Example:
```python
class AccessModifiers:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

    def get_private(self):
        return self.__private

obj = AccessModifiers()
print(obj.public)          # Accessible
print(obj._protected)      # Accessible, but intended for internal use
print(obj.get_private())   # Use a method to access private attributes
```

---

## **Advanced Concepts**
### 1. **Class vs. Instance Attributes**
- Class attributes are shared across all instances.
- Instance attributes are specific to each instance.

### 2. **Using `self` and `cls`**
- `self`: Represents the object instance.
- `cls`: Refers to the class (used in class methods).

### 3. **Multiple Inheritance**
A class can inherit from multiple parents.
```python
class Parent1:
    def method1(self):
        print("From Parent1")

class Parent2:
    def method2(self):
        print("From Parent2")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.method1()  # From Parent1
obj.method2()  # From Parent2
```

### 4. **`super()` Usage**
The `super()` function calls methods from the parent class.
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls Parent's greet
        print("Hello from Child")

obj = Child()
obj.greet()
```

---

## **Comprehensive Example**
```python
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Create objects
dog = Dog("Canine")
cat = Cat("Feline")

print(f"A {dog.species} goes {dog.sound()}")
print(f"A {cat.species} goes {cat.sound()}")
```

---

## **Summary Table**
| Concept          | Description                              | Keyword/Decorator |
|-------------------|------------------------------------------|--------------------|
| Class             | Blueprint for objects                   | `class`           |
| Object            | Instance of a class                     | Instance          |
| Instance Method   | Operates on an object's data            | `self`            |
| Class Method      | Operates on class data                  | `@classmethod`    |
| Static Method     | Independent of the class or object      | `@staticmethod`   |
| Constructor       | Initializes an object                   | `__init__`        |
| Inheritance       | Reuse functionality from another class  | Parentheses       |
| Polymorphism      | Same method, different behavior         | Method Overriding |
| Access Modifiers  | Control access to class data            | `_`, `__`         |

---

## **Additional Theory**
- **Classes and Objects in Large Projects**: Classes act as modular units to organize code efficiently. Multiple objects can collaborate while maintaining independence.
- **Best Practices**:
  1. Use meaningful names for classes and attributes.
  2. Encapsulate data to protect its integrity.
  3. Leverage inheritance and polymorphism effectively for code reuse and readability.
- **Common Mistakes**:
  1. Overusing inheritance when composition is better suited.
  2. Not using encapsulation, leading to inconsistent data.

---

