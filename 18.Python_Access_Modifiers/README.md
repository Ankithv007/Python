# Access Modifiers in Python

Python uses **access modifiers** to define the accessibility or scope of class members (methods and variables). Unlike some languages with strict access control (e.g., Java or C++), Python uses naming conventions to indicate access levels.

## Types of Access Modifiers
1. **Public**  
2. **Protected**  
3. **Private**

---

## 1. Public

### Definition
- Public members are accessible from anywhere — both inside and outside of a class.
- Any attribute or method without a leading underscore (`_`) is considered public by default.

### Syntax
```python
class Example:
    def __init__(self):
        self.public_var = "I am public"  # Public attribute

    def public_method(self):
        print("This is a public method.")
```

### Usage
```python
obj = Example()
print(obj.public_var)  # Accessible directly
obj.public_method()    # Accessible directly
```

---

## 2. Protected

### Definition
- Protected members are indicated by a single leading underscore (`_`) in their names.
- They are meant to be used only within the class and its subclasses.
- Python does not enforce access restrictions for protected members but uses this convention to indicate limited access.

### Syntax
```python
class Example:
    def __init__(self):
        self._protected_var = "I am protected"  # Protected attribute

    def _protected_method(self):
        print("This is a protected method.")
```

### Usage
```python
class Derived(Example):
    def access_protected(self):
        print(self._protected_var)
        self._protected_method()

obj = Derived()
obj.access_protected()    # Accessible in subclass
print(obj._protected_var)  # Technically accessible, but discouraged
```

---

## 3. Private

### Definition
- Private members are indicated by a double leading underscore (`__`) in their names.
- These members cannot be accessed directly from outside the class. Python performs **name mangling** to restrict access.

### Syntax
```python
class Example:
    def __init__(self):
        self.__private_var = "I am private"  # Private attribute

    def __private_method(self):
        print("This is a private method.")

    def access_private(self):
        print(self.__private_var)
        self.__private_method()
```

### Usage
```python
obj = Example()
obj.access_private()  # Allowed: Access through a public method
# print(obj.__private_var)  # AttributeError: Cannot access directly
# obj.__private_method()    # AttributeError: Cannot access directly

# Access using name mangling (not recommended):
print(obj._Example__private_var)
obj._Example__private_method()
```

---

## Key Points to Remember
- **Public**: No underscore. Accessible everywhere.
- **Protected**: Single leading underscore. Suggested use within the class and its subclasses.
- **Private**: Double leading underscore. Limited to the class due to name mangling.

---

## Name Mangling Mechanism
Private attributes (`__name`) are internally renamed as `_ClassName__name`. This discourages access but does not make it completely impossible.

### Example
```python
class Example:
    def __init__(self):
        self.__hidden = "Hidden attribute"

obj = Example()
print(obj._Example__hidden)  # Access using name mangling
```

---

## Why Python Uses This System
1. **Philosophy**: Python follows the "we are all consenting adults here" philosophy, encouraging developers to rely on convention over enforcement.
2. **Flexibility**: Developers can still access restricted members if absolutely necessary.

If strict access control is essential, other techniques like properties, descriptors, or metaclasses can be used in Python.
