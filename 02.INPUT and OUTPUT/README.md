# Input and Output in Python

This document provides an overview of how to handle input and output in Python.

## 1. Introduction
In Python, input and output are essential for interacting with the user and external systems. Input can be received from the user through the console, and output can be displayed to the console or written to files.

## 2. Input in Python
Python provides a built-in function `input()` for getting input from the user. The function waits for the user to enter data, which is then returned as a string.

### Syntax:
```python
input(prompt)

# Prompt the user to enter their name
name = input("Enter your name: ")
print("Hello, " + name)

## Example: Input with Conversion (Integer)
To convert input into another data type (e.g., integer), you can use int() or float().

age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

## Example: Input with Multiple Values
You can accept multiple inputs by splitting the string.
# Accept multiple values separated by space
values = input("Enter space-separated numbers: ").split()
print("You entered:", values)

3. Output in Python
Output in Python is mainly handled using the print() function. It displays the result to the console or terminal.

print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

- value: Values to be printed.
- sep: Separator between values. Default is a space (' ').
- end: What to print at the end. Default is a newline ('\n').
- file: Where to send the output. Default is the console (sys.stdout).
- flush: Whether to forcibly flush the output buffer. Default is False.


## Example: Basic Output
print("Hello, World!")

## Example: Output with Multiple Values
You can print multiple values separated by a custom separator.
print("Name:", name, "Age:", age, sep=" | ")

## Example: Output with Custom End
Change the default newline ending to something else.
print("Hello", end=" ")
print("World!")

4. File Input and Output
Writing to a File
Python provides the open() function to interact with files. You can write to a file using the write() or writelines() methods.
 
 # synatx
with open('filename.txt', 'w') as file:
    file.write("Hello, File!")

- 'w': Write mode (overwrites the file if it exists).
- 'a': Append mode (adds to the file instead of overwriting).

