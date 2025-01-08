# Python Method Overriding

## Introduction
Method overriding in Python is a feature of object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This helps in modifying or extending the behavior of inherited methods.

## What is Method Overriding?
Method overriding occurs when a subclass defines a method with the same name, signature, and parameters as a method in its superclass. This allows the subclass to implement its own behavior, replacing the inherited method’s behavior.

### Key Points:
- The method in the subclass must have the same name and parameters as the method in the superclass.
- The overriding method in the subclass provides a new implementation for the inherited method.
- The method in the subclass can call the method from the superclass using `super()`.
  
## Example of Method Overriding

### Superclass:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    # Overriding the speak method of Animal class
    def speak(self):
        print("Dog barks")

# Create an object of Dog
dog = Dog()
dog.speak()  # Output: Dog barks
```
# Method Overriding with Arguments
```python
class Animal:
    def sound(self, sound_type):
        print(f"Animal makes a {sound_type} sound.")

class Dog(Animal):
    def sound(self, sound_type):
        print(f"Dog makes a {sound_type} sound.")

dog = Dog()
dog.sound("barking")  # Output: Dog makes a barking sound.
```
# Rules for Method Overriding
- The method name, parameters, and return type should match in both the superclass and subclass.
- The access modifier of the method in the subclass should be the same or more accessible than in the superclass (i.e., private methods in the superclass cannot be overridden by public methods in the subclass).
- The method in the subclass is typically called using an instance of the subclass.
 