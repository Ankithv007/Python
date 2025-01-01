# Python Inheritance

Inheritance in Python is a mechanism where one class (child class) derives or inherits the properties and behavior (methods and attributes) from another class (parent class). It enables code reusability and establishes a relationship between classes.

## **Key Features of Inheritance**

1. **Parent and Child Classes**: The parent class contains common attributes and methods, which are inherited by the child class.
2. **Code Reusability**: Features defined in the parent class can be reused, reducing redundancy.
3. **Overriding Methods**: A child class can redefine or override methods from the parent class.
4. **Access Control**: Private attributes and methods in the parent class are not inherited by default.
5. **Extensibility**: New attributes or methods can be added in the child class without affecting the parent class.

## **Types of Inheritance**

### 1. **Single Inheritance**
A child class inherits from only one parent class.

```python
class Parent:
    def display(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

obj = Child()
obj.display()  # Output: Parent class
obj.show()     # Output: Child class
```

---

### 2. **Multiple Inheritance**
A child class inherits from more than one parent class.

```python
class ClassA:
    def method_a(self):
        print("Method from Class A")

class ClassB:
    def method_b(self):
        print("Method from Class B")

class ClassC(ClassA, ClassB):
    pass

obj = ClassC()
obj.method_a()  # Output: Method from Class A
obj.method_b()  # Output: Method from Class B
```

---

### 3. **Multilevel Inheritance**
A class inherits from a child class, creating a chain.

```python
class Grandparent:
    def method_gp(self):
        print("Grandparent method")

class Parent(Grandparent):
    def method_p(self):
        print("Parent method")

class Child(Parent):
    def method_c(self):
        print("Child method")

obj = Child()
obj.method_gp()  # Output: Grandparent method
obj.method_p()   # Output: Parent method
obj.method_c()   # Output: Child method
```

---

### 4. **Hierarchical Inheritance**
Multiple child classes inherit from one parent class.

```python
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class Bike(Vehicle):
    def ride(self):
        print("Bike rides")

car = Car()
car.start()  # Output: Vehicle starts
car.drive()  # Output: Car drives

bike = Bike()
bike.start() # Output: Vehicle starts
bike.ride()  # Output: Bike rides
```

---

### 5. **Hybrid Inheritance**
A mix of two or more types of inheritance, forming a complex hierarchy.

```python
class Base:
    def method_base(self):
        print("Base method")

class Child1(Base):
    pass

class Child2(Base):
    pass

class GrandChild(Child1, Child2):
    pass

obj = GrandChild()
obj.method_base()  # Output: Base method
```

---

## **Key Concepts in Inheritance**

### **`super()` Keyword**
The `super()` function is used to call a method from the parent class.

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Call Parent's greet method
        print("Hello from Child")

obj = Child()
obj.greet()
# Output:
# Hello from Parent
# Hello from Child
```

### **Method Overriding**
A child class can override methods from the parent class.

```python
class Parent:
    def display(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")

obj = Child()
obj.display()  # Output: Child class
```

### **The `isinstance()` and `issubclass()` Functions**
- **`isinstance(obj, Class)`**: Checks if an object is an instance of a class.
- **`issubclass(Class1, Class2)`**: Checks if Class1 is a subclass of Class2.

```python
class Parent:
    pass

class Child(Parent):
    pass

obj = Child()
print(isinstance(obj, Child))   # Output: True
print(isinstance(obj, Parent)) # Output: True
print(issubclass(Child, Parent)) # Output: True
```

---

## **Practical Example**
Here is an example combining inheritance concepts:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

manager = Manager("Ankith", 70000, 10)
manager.show_details()
# Output:
# Name: Ankith, Salary: 70000
# Team Size: 10
