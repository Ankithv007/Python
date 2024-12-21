# Python Modules

## Overview
Python modules are files containing Python code, typically functions, classes, or variables, to organize related functionalities and improve code reusability. These modules can be built-in, standard, or custom-made.

## Why Use Modules?
- To organize code into logical segments.
- To enhance reusability and reduce redundancy.
- To maintain and debug code effectively.

---

## Types of Modules

### 1. Built-in Modules
These modules are included in the Python standard library and don't require additional installation. Examples: `math`, `os`, `sys`, `random`.

#### Example: Using the `math` Module
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### 2. Standard Modules (3rd-party)
These are available via the Python Package Index (PyPI) and can be installed using tools like `pip`. Examples: `numpy`, `pandas`, `requests`.

#### Example: Installing and Using `requests`
```bash
pip install requests
```
```python
import requests
response = requests.get('https://api.github.com')
print(response.status_code)
```

### 3. Custom Modules 
You can create your own modules by saving Python code in a `.py` file and importing it into other scripts.

#### Example: Creating and Using a Custom Module
**Module File**: `my_module.py`
```python
def greet(name):
    return f"Hello, {name}!"
```
**Main Script**:
```python
import my_module
print(my_module.greet("Ankith"))  # Output: Hello, Ankith!
```

---

## Common Built-in Modules

### os
- Provides a way to interact with the operating system.
```python
import os
print(os.getcwd())  # Current working directory
```

### sys
- Deals with system-specific parameters and functions.
```python
import sys
print(sys.version)  # Python version
```

### math
- Performs mathematical operations.
```python
import math
print(math.pi)  # 3.141592653589793
```

### random
- Generates random numbers.
```python
import random
print(random.randint(1, 10))
```

---

## Creating Custom Python Modules

### Steps to Create and Import
1. Write functions/classes in a `.py` file (module).
2. Save the file in the desired directory.
3. Import it using `import module_name`.

### Adding `__init__.py` to a Package
Combine modules into packages using an `__init__.py` file.

#### Folder Structure Example
```plaintext
my_package/
    __init__.py
    module1.py
    module2.py
```
**Usage:**
```python
from my_package.module1 import my_function
```

---

## Packaging and Distributing Python Modules

### Packaging Steps
1. Create a `setup.py` file with package details.
2. Use tools like `setuptools` or `distutils`.
3. Upload your package to PyPI for distribution.

#### Example: `setup.py`
```python
from setuptools import setup
setup(
    name='my_package',
    version='1.0.0',
    description='An example Python package',
    author='Ankith B V',
    packages=['my_package'],
)
```

### Installation
```bash
pip install my_package
```

---

## Best Practices

- Follow Python's naming conventions for modules (`snake_case`).
- Keep the module's functionality focused on a single aspect or related set of features.
- Use proper documentation in each module.
- Handle imports carefully to avoid circular dependencies.
- Test modules thoroughly before using them in production.

---

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/tutorial/modules.html)
- [PyPI - Python Package Index](https://pypi.org)
