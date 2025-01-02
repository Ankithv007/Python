# Python Encapsulation

Encapsulation is a fundamental principle of object-oriented programming (OOP) in Python that restricts direct access to an object's data and methods, ensuring better control and security of data.

---

## Key Concepts

### 1. Access Specifiers
Python uses underscores (`_` or `__`) to define the visibility of variables and methods:
- **Public (`no underscore`)**: Accessible from outside the class.
- **Protected (`_single_underscore`)**: For internal use but can still be accessed.
- **Private (`__double_underscore`)**: Name-mangled to prevent direct access from outside the class.

### 2. Data Hiding
Private attributes ensure that data cannot be modified directly. Instead, access or modification is done using getter and setter methods.

### 3. Getter and Setter Methods
- **Getter**: Retrieves the value of a private variable.
- **Setter**: Updates the value of a private variable after validation.

### 4. Name Mangling
Private attributes use name mangling to make their names unique: `_ClassName__AttributeName`.

---

## Examples

### Public Attributes
```python
class PublicExample:
    def __init__(self):
        self.data = "I am accessible anywhere"

obj = PublicExample()
print(obj.data)  # Output: I am accessible anywhere
```

### Protected Attributes
```python
class ProtectedExample:
    def __init__(self):
        self._data = "I am for internal use only"

obj = ProtectedExample()
print(obj._data)  # Output: I am for internal use only (accessible but discouraged)
```

### Private Attributes
```python
class PrivateExample:
    def __init__(self):
        self.__data = "I am private"

obj = PrivateExample()
# print(obj.__data)  # AttributeError: 'PrivateExample' object has no attribute '__data'
print(obj._PrivateExample__data)  # Output: I am private (accessed through name mangling)
```

### Encapsulation with Getter and Setter
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount!")

    def get_balance(self):  # Getter
        return self.__balance

# Usage
account = BankAccount()
account.deposit(500)
print(account.get_balance())  # Output: 500
account.withdraw(200)
print(account.get_balance())  # Output: 300
```

---

## Advantages

1. **Data Security**: Prevents unauthorized access.
2. **Modularization**: Simplifies object complexity by abstracting details.
3. **Validation**: Ensures valid data using setter methods.
4. **Reusability**: Encapsulated code is easier to reuse in multiple places.

---

## Best Practices

- Use **public attributes** only for data meant to be accessible globally.
- Use **protected attributes** to signal that variables/methods should not be directly accessed but can be overridden in subclasses.
- Use **private attributes** to secure sensitive data.
- Employ getter and setter methods to maintain control over attribute modification.
