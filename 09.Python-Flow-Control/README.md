# Python Flow Control

## Introduction
Flow control in Python determines the execution order of instructions in a program. It consists of conditional statements, loops, and control transfer statements, enabling developers to create dynamic and flexible programs.

---

## Types of Flow Control Statements

1. Conditional Statements
Control the flow of execution based on conditions:

#### If Statement:
Executes a block of code if the condition is true.
```python
if condition:
    # Code to execute
```
### If-Else Statement:
Provides an alternative block of code when the condition is false
```python
if condition:
    # Code if condition is true
else:
    # Code if condition is false
```
### If-Elif-Else Statement:
Allows multiple conditions to be checked sequentially.
```python
if condition1:
    # Code for condition1
elif condition2:
    # Code for condition2
else:
    # Code if none are true

```
2. Loops
Repeat a block of code as long as a condition is met.
 
### For Loop: 
Iterates over a sequence (like lists, tuples, strings, etc.).
```python
for variable in sequence:
    # Code to execute
```
### While Loop:
Continues execution as long as the condition is true.
```python
while condition:
    # Code to execute

```
3. Control Transfer Statements
Alter the normal flow of loops and conditionals.

### Break Statement:
Exits the loop prematurely.
```python 
for i in range(10):
    if i == 5:
        break
```
### Continue Statement:
Skips the current iteration and continues with the next.
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

```
### Pass Statement:
Does nothing; acts as a placeholder
```python
if condition:
    pass  # Code to be implemented later
```
### Else with Loops:
Executes a block of code if the loop completes without a break.
```python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

```
---

# examples
### Example 1: Check If a Number is Positive or Negative
```python
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```
### Example 2: Print Odd Numbers in a Range
```python
for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)

```    





