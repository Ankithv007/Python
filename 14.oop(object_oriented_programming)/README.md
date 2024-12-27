# Object-Oriented Programming (OOP) in Python

## Overview
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of **"objects"**, which are collections of **attributes** (data) and **methods** (functions that act on the data). 

In OOP, you model real-world entities as objects and define their behavior and interaction. Python supports OOP fully, enabling code reuse, modular design, and better abstraction.

---

## Key Concepts of OOP

### 1. **Class**
   - A **class** is a blueprint for creating objects. It defines the structure (attributes) and behavior (methods) of the objects.
   - Example:
     ```python
     class Car:
         def __init__(self, brand, model):
             self.brand = brand
             self.model = model
         
         def display_info(self):
             print(f"Car Brand: {self.brand}, Model: {self.model}")
     ```

### 2. **Object**
   - An **object** is an instance of a class. It has a unique identity and holds the data defined by its class.
   - Example:
     ```python
     my_car = Car("Toyota", "Corolla")  # Creating an object
     my_car.display_info()
     ```

### 3. **Attributes and Methods**
   - **Attributes**: Variables that belong to an object. They represent the object's state or properties.
   - **Methods**: Functions defined inside a class that operate on the object's attributes.
   - Example:
     ```python
     class Dog:
         def __init__(self, name, age):
             self.name = name    # Attribute
             self.age = age      # Attribute

         def bark(self):         # Method
             print(f"{self.name} says Woof!")
     ```

### 4. **Encapsulation**
   - Encapsulation means bundling the data (attributes) and methods into a single unit (class) and restricting direct access to some of the object's data.
   - **Access Modifiers**:
     - `public`: Accessible from anywhere (default).
     - `protected` (convention: single underscore `_`): Intended for internal use but can be accessed.
     - `private` (convention: double underscore `__`): Cannot be accessed directly outside the class.
   - Example:
     ```python
     class Person:
         def __init__(self, name, age):
             self.__age = age  # Private attribute

         def get_age(self):    # Getter method
             return self.__age
         
         def set_age(self, age):  # Setter method
             if age > 0:
                 self.__age = age
     ```

### 5. **Inheritance**
   - Inheritance allows a class (**child**) to inherit the properties and methods of another class (**parent**). It helps promote code reuse.
   - Types of Inheritance:
     1. Single Inheritance: One child, one parent.
     2. Multiple Inheritance: A class inherits from multiple parents.
     3. Multilevel Inheritance: Inheriting from a child class.
   - Example:
     ```python
     class Animal:
         def speak(self):
             print("Animal speaks")
         
     class Dog(Animal):  # Single inheritance
         def speak(self):
             print("Dog barks")

     my_dog = Dog()
     my_dog.speak()
     ```

### 6. **Polymorphism**
   - Polymorphism allows the same method to behave differently based on the object it is called on. This can be achieved using **method overriding**.
   - Example:
     ```python
     class Shape:
         def area(self):
             pass
         
     class Square(Shape):
         def __init__(self, side):
             self.side = side
         
         def area(self):
             return self.side ** 2
         
     class Circle(Shape):
         def __init__(self, radius):
             self.radius = radius
         
         def area(self):
             return 3.14 * self.radius ** 2

     shapes = [Square(4), Circle(3)]
     for shape in shapes:
         print(shape.area())  # Outputs: 16 and 28.26
     ```

### 7. **Abstraction**
   - Abstraction hides implementation details and shows only essential features to the user. In Python, you can achieve abstraction using abstract base classes (`ABC` module).
   - Example:
     ```python
     from abc import ABC, abstractmethod

     class Animal(ABC):
         @abstractmethod
         def sound(self):
             pass
         
     class Cat(Animal):
         def sound(self):
             return "Meow"
         
     my_cat = Cat()
     print(my_cat.sound())  # Outputs: Meow
     ```

---

## Other OOP Features in Python

### 1. **Constructors**
   - The `__init__` method is the constructor in Python and is called automatically when creating an object.

### 2. **Destructors**
   - The `__del__` method acts as a destructor, called when the object is deleted or goes out of scope.

### 3. **Operator Overloading**
   - Python allows overloading operators to provide user-defined behaviors.
   - Example:
     ```python
     class Point:
         def __init__(self, x, y):
             self.x = x
             self.y = y
         
         def __add__(self, other):
             return Point(self.x + other.x, self.y + other.y)
         
     p1 = Point(1, 2)
     p2 = Point(3, 4)
     p3 = p1 + p2  # Calls __add__
     print(p3.x, p3.y)  # Outputs: 4 6
     ```

---

## Advantages of OOP
1. **Modularity**: Code is organized into classes, making it easier to maintain.
2. **Reusability**: Inheritance allows sharing and reusing code efficiently.
3. **Scalability**: Adding new features is simple due to abstraction and modular design.
4. **Maintainability**: Encapsulation simplifies debugging and maintenance.

---

## Common Terms
- **Class Variable vs. Instance Variable**:
  - Class Variable: Shared among all objects (defined within the class).
  - Instance Variable: Specific to each object (defined within methods like `__init__`).
- **Duck Typing**:
  - Python does not enforce strict type checking. If an object performs the required operation, it’s considered valid.
  - Example:
    ```python
    class Bird:
        def fly(self):
            print("Flies")
        
    def make_fly(entity):
        entity.fly()
        
    make_fly(Bird())  # Outputs: Flies
    ```

---

