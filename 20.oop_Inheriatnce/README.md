# Python Inheritance: Complete Overview

Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class (child class) to inherit the properties and methods of another class (parent class). In Python, inheritance enables code reuse, logical structure, and extendability of classes.

---

## Key Features of Inheritance
1. **Reusability**: Use existing class code in a new class.
2. **Overriding**: Redefine parent class methods in the child class for specific behaviors.
3. **Extensibility**: Extend the functionalities of an existing class without modifying it.
4. **Relationships**: Helps establish "is-a" relationships.

---

## Syntax of Inheritance

```python
class ParentClass:
    # Parent class methods and properties
    pass

class ChildClass(ParentClass):
    # Child class methods and properties
    pass
```

---

## Example of Single Inheritance

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Testing
dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog
```

---

## Types of Inheritance in Python

1. **Single Inheritance**  
   One child inherits from one parent.

   ```python
   class A:
       def method_a(self):
           print("Method A")

   class B(A):
       def method_b(self):
           print("Method B")
   ```

2. **Multiple Inheritance**  
   A child inherits from multiple parents.

   ```python
   class A:
       def method_a(self):
           print("Method A")

   class B:
       def method_b(self):
           print("Method B")

   class C(A, B):
       pass

   obj = C()
   obj.method_a()  # From A
   obj.method_b()  # From B
   ```

3. **Multilevel Inheritance**  
   A child inherits from a parent, which is itself a child of another parent.

   ```python
   class A:
       def method_a(self):
           print("Method A")

   class B(A):
       def method_b(self):
           print("Method B")

   class C(B):
       def method_c(self):
           print("Method C")
   ```

4. **Hierarchical Inheritance**  
   Multiple children inherit from the same parent.

   ```python
   class A:
       def method_a(self):
           print("Method A")

   class B(A):
       pass

   class C(A):
       pass
   ```

5. **Hybrid Inheritance**  
   A combination of two or more types of inheritance.

---

## Method Overriding
A child class can override a parent class method to redefine its behavior.

```python
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

child = Child()
child.show()  # Outputs "Child class"
```

---

## The `super()` Function
The `super()` function is used to call methods of the parent class.

```python
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        super().show()  # Calls Parent's show
        print("Child class")

child = Child()
child.show()
```

---

## The `__init__()` Method in Inheritance

The `__init__()` method can be inherited and extended using `super()`.

```python
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call Parent's __init__()
        print("Child constructor")

obj = Child()
```

---

## Access Modifiers in Inheritance
1. **Public Attributes**: Inherited directly.
2. **Protected Attributes** (with `_`): Accessible to the child class.
3. **Private Attributes** (with `__`): Not directly accessible but can be accessed using special methods.

```python
class Parent:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

class Child(Parent):
    def show(self):
        print(self.public)
        print(self._protected)
        # print(self.__private)  # Not accessible

child = Child()
child.show()
```

---

## `isinstance()` and `issubclass()` Functions

1. **`isinstance()`**: Checks if an object is an instance of a class or subclass.

   ```python
   isinstance(obj, ParentClass)
   ```

2. **`issubclass()`**: Checks if a class is a subclass of another class.

   ```python
   issubclass(ChildClass, ParentClass)
   ```

---

## Common Use Cases
1. Building frameworks and libraries (e.g., Flask, Django).
2. Extending functionalities of base classes.
3. Real-world scenarios like:
   - Base class `Vehicle` with subclasses `Car`, `Bike`, `Truck`.

---

