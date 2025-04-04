
# Python Programming Tutorial

This repository contains a Python tutorial covering various foundational concepts, including data types, control structures, functions, file handling, list comprehension, and more. The code examples provided serve as a guide to help you better understand Python's syntax and capabilities for both beginners and intermediate learners.

## Table of Contents
1. [Data Types](#data-types)
2. [Control Structures](#control-structures)
3. [Functions](#functions)
4. [Looping](#looping)
5. [File Handling](#file-handling)
6. [List Comprehension](#list-comprehension)
7. [User Input](#user-input)

## Data Types

In Python, we deal with several basic data types such as integers, strings, floats, lists, dictionaries, and tuples. Here’s how they work:

### Example Code:
```python
# Data types
integer = 10
string = "10"
floatt = 10.1

# List
l = [10, 11, 12, 13, 14, 15]

# String manipulation
var1 = "Hello World!"
up = var1.upper()
print(up)

# List operations
countl = len(l)
summerl = sum(l)
avel = summerl / countl
print(avel)

# Dictionary example
dic = {"Marry": 11.5, "Ali": 15.6, "Inna": 18, "John": 17.5}
sumdic = sum(dic.values())
lendic = len(dic)
meandic = sumdic / lendic
print(meandic)
```

### Explanation:
- **Integer** and **Float** are numeric data types.
- **String** manipulation involves converting to uppercase.
- **List** operations such as calculating the mean.
- **Dictionary** operations like summing values and calculating the mean.

## Control Structures

### Conditionals:

Control the flow of your program using `if` statements to make decisions based on conditions.

### Example Code:
```python
def weather_condition(temp):
    if temp > 7:
        return "warm"
    else:
        return "cold"
```

### Loops:
- **For Loops** and **While Loops** are used to iterate over sequences or run indefinitely under certain conditions.

### Example Code:
```python
username = ''
while username != "pypy":
    username = input("Enter your username: ")
    
while True:
    username = input("Enter your username: ")
    if username == 'pypy':
        break
    else:
        continue
```

## Functions

Functions help you organize your code into reusable blocks. You can pass parameters to a function and return values.

### Example Code:
```python
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([10, 15, 17, 18, 13, 19]))

# Function with default parameters
def example(a, b=3):
    return a * b

print(example(5, 2))
print(example(5))

# Function with arbitrary arguments (*args and **kwargs)
def mean4(*args):
    return args

print(mean4(1, 2, 3, 'e', 5))

def mean3(**kwargs):
    return kwargs

print(mean3(a=2, b=1, c='d'))
```

### Explanation:
- **Default Parameters** allow a function to accept optional arguments.
- **Arbitrary Arguments** (`*args` and `**kwargs`) let you pass an arbitrary number of arguments to a function.

## Looping

Python provides two types of loops: **for loops** and **while loops**.

### Example Code:
```python
# While Loop Example
username = ''
while username != "pypy":
    username = input("Enter your username: ")

# Infinite Loop
while True:
    username = input("Enter your username: ")
    if username == 'pypy':
        break
    else:
        continue
```

### Explanation:
- **While Loops** continue to execute until a condition is met.
- **For Loops** iterate over collections like lists or strings.

## File Handling

Python allows you to interact with files to read, write, and modify content.

### Example Code:
```python
# Reading a file
with open("file3.txt") as myfile:
    content = myfile.read()
    print(content)

# Writing to a file
with open("file3.txt", "w") as myfile:
    myfile.write("Hello, World!
")
```

### Explanation:
- **Reading** and **writing** files are done using `open()`.
- Use **`with`** to ensure files are properly closed after usage.

## List Comprehension

List comprehension provides a concise way to create lists by applying operations to each element.

### Example Code:
```python
temps = [221, 331, 141, 122]

# Basic list comprehension
new_temps = [temp / 10 for temp in temps]
print(new_temps)

# Using if condition
new_temps = [temp / 10 for temp in temps if temp != 141]
print(new_temps)

# Using if-else condition
new_temps = [temp / 10 if temp != 141 else 0 for temp in temps]
print(new_temps)
```

### Explanation:
- **List Comprehension** allows efficient operations on lists.
- **Conditional Statements** can be used inside list comprehensions to filter or modify elements.

## User Input

You can accept user input using `input()` and convert it to specific data types as needed.

### Example Code:
```python
name = input("Enter your name: ")
message = f"Hello {name}"
print(message)
```

### Explanation:
- `input()` captures user input as a string, which can be converted to other types like `int()` or `float()`.

---

## Conclusion

This repository contains a variety of Python concepts to help you get started with programming. Whether you're learning basic data types, exploring control structures, or diving into file handling and list comprehensions, these examples will give you the foundation you need to build more complex programs.
