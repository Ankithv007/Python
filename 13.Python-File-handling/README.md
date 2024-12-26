# Python File Handling Guide

File handling in Python involves managing files such as reading, writing, and manipulating them. Python's built-in `open()` function provides an interface to access and manage files.

---

## 1. Basic Concepts

### Modes for File Opening:
| Mode    | Description                                           |
|---------|-------------------------------------------------------|
| `'r'`   | Open a file for reading (default). File must exist.   |
| `'w'`   | Open a file for writing. Creates a new file if it doesn’t exist; truncates if it does. |
| `'x'`   | Open a file for exclusive creation. Fails if file exists. |
| `'a'`   | Open for writing; appends to the end if the file exists. |
| `'b'`   | Binary mode.                                           |
| `'t'`   | Text mode (default).                                  |
| `'+'`   | Open for reading and writing.                        |

---

## 2. Basic Syntax
```python
# Syntax:
file = open('filename', 'mode')

# Example:
file = open('example.txt', 'r')  # Opens the file in read mode
file.close()                     # Always close the file after operations
```

---

## 3. File Reading Methods

| Method                   | Description                                     |
|--------------------------|-------------------------------------------------|
| `file.read(size=-1)`     | Reads the entire file or the specified number of bytes. |
| `file.readline(size=-1)` | Reads one line from the file.                   |
| `file.readlines()`       | Reads all lines into a list.                   |

### Example:
```python
with open('example.txt', 'r') as file:
    content = file.read()  # Reads the entire file
    print(content)

# Read line-by-line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Reads lines one by one
```

---

## 4. File Writing Methods

| Method               | Description                                       |
|----------------------|---------------------------------------------------|
| `file.write(text)`   | Writes the given text to the file.                |
| `file.writelines(seq)` | Writes a sequence of strings to the file.        |

### Example:
```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\nThis is a test.")

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\nAppended Text!")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)
```

---

## 5. File Manipulation

### Check if File Exists:
Use the `os` module to verify file existence.
```python
import os

if os.path.exists('example.txt'):
    print("File exists!")
else:
    print("File does not exist!")
```

---

### Delete a File:
```python
os.remove('example.txt')
```

---

### Rename a File:
```python
os.rename('old.txt', 'new.txt')
```

---

## 6. File Pointers
File objects have an internal pointer to manage the current position.

| Method               | Description                                         |
|----------------------|-----------------------------------------------------|
| `file.tell()`        | Returns the current position of the file pointer.   |
| `file.seek(offset, from)` | Changes the file pointer position (absolute or relative). |

```python
with open('example.txt', 'r') as file:
    print(file.tell())  # Get current position
    file.seek(0)        # Move to the start
```

---

## 7. Binary File Operations

Binary files store data like images and audio. Open the file in binary mode using `'b'`.

```python
# Writing a binary file
data = b'\xDE\xAD\xBE\xEF'
with open('binaryfile.bin', 'wb') as file:
    file.write(data)

# Reading a binary file
with open('binaryfile.bin', 'rb') as file:
    content = file.read()
    print(content)
```

---

## 8. Exception Handling in File Operations
```python
try:
    with open('nonexistent.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## 9. CSV File Handling
Use the `csv` module to handle CSV files.
```python
import csv

# Writing CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])

# Reading CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## 10. JSON File Handling
Use the `json` module for JSON file operations.
```python
import json

# Writing JSON
data = {"name": "John", "age": 30, "city": "New York"}
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading JSON
with open('data.json', 'r') as file:
    content = json.load(file)
    print(content)
```

---

### Best Practices:
1. Always use the `with` statement to automatically close files.
2. Use exception handling to handle file-related errors.
3. Check file existence before performing destructive operations.
4. Prefer absolute paths to avoid confusion with relative paths.
5. Avoid hardcoding paths; use `os.path` for compatibility.

---
