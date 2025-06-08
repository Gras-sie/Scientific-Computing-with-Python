# Scientific Computing with Python - Comprehensive Cheat Sheet

This repository contains various Python projects demonstrating scientific computing concepts. Below is a comprehensive cheat sheet covering all Python concepts used throughout the codebase, with detailed explanations and references to example files.

## Table of Contents
- [Basic Python Concepts](#basic-python-concepts)
- [Data Structures](#data-structures)
- [String Operations](#string-operations)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Functional Programming](#functional-programming)
- [File Operations](#file-operations)
- [Modules and Imports](#modules-and-imports)
- [Error Handling](#error-handling)
- [Regular Expressions](#regular-expressions)
- [Algorithms](#algorithms)
- [Project-Specific Concepts](#project-specific-concepts)

## Basic Python Concepts

### Variables
- **What they are**: Variables are named references to memory locations where data values are stored. Python is dynamically typed, meaning you don't need to declare a variable's type; it's inferred at runtime.
- **How they work**: You assign a value to a variable using the assignment operator (`=`). Python handles memory allocation automatically. It's a convention (PEP 8) to use `snake_case` for variable names (e.g., `my_variable`).
- **Example**:
```python
my_variable = 42  # Integer
name = "John"     # String
is_valid = True   # Boolean
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `letters`, `digits`, `password`)

### Data Types
- **What they are**: Fundamental categories of data. Python has several built-in data types.
    - **Integers (`int`)**: Whole numbers, positive or negative (e.g., `42`, `-7`).
    - **Floats (`float`)**: Numbers with a decimal point (e.g., `3.14`, `-0.001`).
    - **Strings (`str`)**: Sequences of characters, immutable (e.g., `"Hello"`, `'World'`).
    - **Booleans (`bool`)**: Represent truth values, `True` or `False`.
    - **None (`NoneType`)**: Represents the absence of a value or a null value.
- **How they work**: Python automatically determines the data type when you assign a value. You can convert between compatible types using built-in functions like `int()`, `float()`, `str()`.
- **Example**:
```python
# Type conversion
str_num = "42"
num = int(str_num)          # Convert string to integer
float_num = float(str_num)  # Convert string to float
is_true = bool(1)           # Convert integer to boolean (0 is False, others True)
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., string literals, integer parameters)

## Data Structures

### Lists
- **What they are**: Ordered, mutable (changeable) collections of items. Lists can contain items of different data types.
- **How they work**: Defined using square brackets `[]`. Items are accessed by their index (starting from 0).
    - `my_list[0]` accesses the first item.
    - `my_list.append(item)` adds an item to the end.
    - `my_list.insert(index, item)` inserts an item at a specific position.
    - `my_list.pop()` removes and returns the last item.
    - `len(my_list)` returns the number of items.
- **Example**:
```python
my_list = [1, 2, 3, "hello"]
first_item = my_list[0]      # Accesses 1
my_list.append(4)            # my_list is now [1, 2, 3, "hello", 4]
my_list[1] = "world"         # my_list is now [1, "world", 3, "hello", 4]
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `constraints` list)

### List Comprehensions
- **What they are**: A concise and readable way to create lists. Often more efficient than using explicit `for` loops and `append`.
- **How they work**: The basic syntax is `[expression for item in iterable if condition]`. The `if condition` part is optional.
- **Example**:
```python
squares = [x**2 for x in range(10)]  # Creates [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(10) if x % 2 == 0]  # Creates [0, 2, 4, 6, 8]
```
- **Where to find examples**: Coming Soon.

### Tuples
- **What they are**: Ordered, immutable (unchangeable) sequences of items. Often used for fixed collections of items or when you want to ensure data doesn't change.
- **How they work**: Defined using parentheses `()`. Like lists, items are accessed by index. Tuple packing is when you assign a sequence of values to a tuple, and unpacking is assigning tuple elements to individual variables.
- **Example**:
```python
point = (10, 20)      # Tuple packing
x, y = point          # Tuple unpacking (x=10, y=20)
# point[0] = 5       # This would raise a TypeError because tuples are immutable
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., items in the `constraints` list like `(nums, r'\d')`)

### Dictionaries
- **What they are**: Unordered (in Python < 3.7) or ordered (Python 3.7+) collections of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples). Dictionaries are mutable.
- **How they work**: Defined using curly braces `{}` with `key: value` items. Values are accessed using their keys.
    - `person["name"]` accesses the value associated with the key "name".
    - `person.get("key", default_value)` safely gets a value.
    - `person.keys()`, `person.values()`, `person.items()`.
- **Example**:
```python
person = {"name": "Alice", "age": 30}
name = person["name"]                 # Accesses "Alice"
person["email"] = "alice@example.com" # Adds a new key-value pair
person["age"] = 31                    # Updates the value for "age"
```
- **Where to find examples**: Coming Soon.

### Sets
- **What they are**: Unordered collections of unique, immutable items. Useful for membership testing and eliminating duplicate entries.
- **How they work**: Defined using curly braces `{}` or the `set()` function. Mathematical set operations like union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`) are supported.
- **Example**:
```python
unique_numbers = {1, 2, 3, 3, 2}  # Results in {1, 2, 3}
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2           # {1, 2, 3, 4, 5}
intersection_set = set1 & set2    # {3}
```
- **Where to find examples**: Coming Soon.

## String Operations

### String Methods
- **What they are**: Built-in functions that operate on strings. Since strings are immutable, these methods return new strings rather than modifying the original.
- **How they work**: Called using dot notation on a string variable (e.g., `text.lower()`).
    - `.lower()`, `.upper()`: Convert case.
    - `.replace(old, new)`: Replace occurrences of a substring.
    - `.strip()`: Remove leading/trailing whitespace.
    - `.split(separator)`: Split string into a list of substrings.
    - `.join(iterable)`: Join elements of an iterable into a string.
    - `.find(substring)`: Find first occurrence of a substring.
- **Example**:
```python
text = "  Hello, World!  "
lower_text = text.lower()          # "  hello, world!  "
stripped_text = text.strip()       # "Hello, World!"
parts = stripped_text.split(", ")   # ["Hello", "World!"]
joined_text = "-".join(parts)      # "Hello-World!"
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `string.ascii_letters`, `string.digits`, `string.punctuation` are strings with useful properties)

### String Formatting
- **What it is**: Creating strings by embedding expressions or variables within them.
- **How it works**:
    - **f-strings (Formatted String Literals, Python 3.6+)**: Prefix string with `f` or `F`. Expressions in `{}` are evaluated at runtime. Most modern and preferred method.
    - **`str.format()` method**: Placeholders `{}` are replaced by arguments to `.format()`.
    - **`%` operator (older style)**: Similar to C's `printf`.
- **Example**:
```python
name = "Alice"
age = 30
# f-strings
message_f = f"{name} is {age} years old. Next year she'll be {age + 1}."
# format method
message_format = "{} is {} years old.".format(name, age)
# % formatting
message_percent = "%s is %d years old." % (name, age)
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `fr'[{symbols}]'` in constraints, `print('Generated password:', new_password)`)

### String Slicing
- **What it is**: Extracting a portion (substring) from a string.
- **How it works**: Uses the syntax `string[start:stop:step]`.
    - `start`: The starting index (inclusive). Defaults to 0.
    - `stop`: The ending index (exclusive). Defaults to the end of the string.
    - `step`: The increment between indices. Defaults to 1.
    - Negative indices count from the end of the string.
- **Example**:
```python
text = "Hello, World!"
first_five = text[0:5]     # "Hello" (or text[:5])
world_part = text[7:12]    # "World"
from_end = text[-6:]       # "World!"
every_other = text[::2]    # "Hlo ol!"
reversed_text = text[::-1] # "!dlroW ,olleH"
```
- **Where to find examples**: Coming Soon.

## Control Flow

### Conditionals
- **What they are**: Statements that allow your program to execute different blocks of code based on whether certain conditions are true or false.
- **How they work**:
    - `if condition:`: Executes the block if `condition` is true.
    - `elif another_condition:`: (Else if) Executes if the previous `if` or `elif` conditions were false, and `another_condition` is true.
    - `else:`: Executes if all preceding `if` and `elif` conditions were false.
    - Conditions evaluate to boolean values (`True` or `False`). Python considers values like `0`, `None`, empty sequences (e.g., `""`, `[]`, `{}`) as "falsy", and most other values as "truthy".
- **Example**:
```python
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `if all(...)`)

### Loops
- **What they are**: Structures for repeatedly executing a block of code.
- **How they work**:
    - **`for` loop**: Iterates over a sequence (like a list, tuple, string, or range) or other iterable objects.
        ```python
        for item in my_list:
            print(item)
        for i in range(5):  # Iterates from 0 to 4
            print(i)
        ```
    - **`while` loop**: Repeats a block of code as long as a condition is true.
        ```python
        count = 0
        while count < 5:
            print(count)
            count += 1  # Important to update the condition variable
        ```
    - **Control statements**:
        - `break`: Exits the current loop immediately.
        - `continue`: Skips the rest of the current iteration and proceeds to the next.
        - `else` clause: Can be used with loops. For `for` loops, it executes if the loop completed normally (no `break`). For `while` loops, it executes if the condition became false (no `break`).
- **Example**:
```python
# For loop
for i in range(5):
    if i == 3:
        break  # Exits when i is 3
    print(i)  # Prints 0, 1, 2

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop finished normally")
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `while True:`, `for _ in range(length):`, `for constraint, pattern in constraints`)

### Comprehensions
- **What they are**: A concise way to create lists, sets, or dictionaries. They often provide a more readable and Pythonic alternative to using explicit loops for creating these data structures.
- **How they work**:
    - **List comprehension**: `[expression for item in iterable if condition]`
    - **Set comprehension**: `{expression for item in iterable if condition}`
    - **Dictionary comprehension**: `{key_expression: value_expression for item in iterable if condition}`
- **Example**:
```python
# List comprehension (already shown)
squares_list = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Set comprehension
squares_set = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
- **Where to find examples**: The generator expression `(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints)` inside `all()` in `Pasword_Generator.py` is similar in concept. Full list/dict/set comprehensions: Coming Soon.

## Functions

### Basic Functions
- **What they are**: Reusable blocks of code that perform a specific task. Functions help organize code, make it more modular, and promote the DRY (Don't Repeat Yourself) principle.
- **How they work**:
    - Defined using the `def` keyword, followed by the function name, parentheses `()` for parameters, and a colon `:`.
    - The code block within the function is indented.
    - **Parameters**: Variables listed inside the parentheses in the function definition.
    - **Arguments**: Actual values passed to the function when it is called.
    - `return` statement: Exits the function and optionally sends a value back to the caller. If no `return` statement is present or `return` is used without a value, the function returns `None`.
    - **Docstrings**: A string literal as the first statement in a function's body, used to document the function's purpose, arguments, and return value.
- **Example**:
```python
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"

message = greet("Alice")  # Calling the function
print(message)            # Output: Hello, Alice!
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `def generate_password(...)`)

### Default Parameters
- **What they are**: Parameters that take a default value if no argument is supplied for them when the function is called.
- **How they work**: You specify default values in the function definition using the assignment operator `=`. Parameters with default values must come after parameters without default values.
- **Example**:
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))            # Output: Hello, Bob!
print(greet("Charlie", "Hi"))  # Output: Hi, Charlie!
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `length=16, nums=1, ...` in `generate_password`)

### *args and **kwargs
- **What they are**: Special syntax to allow functions to accept a variable number of arguments.
- **How they work**:
    - **`*args` (Arbitrary Positional Arguments)**: Collects extra positional arguments passed to the function into a tuple. The name `args` is a convention; you can use other names (e.g., `*numbers`).
    - **`**kwargs` (Arbitrary Keyword Arguments)**: Collects extra keyword arguments passed to the function into a dictionary. The name `kwargs` is a convention.
- **Example**:
```python
# *args
def sum_all(*numbers):  # numbers will be a tuple
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_all(1, 2, 3))  # Output: 6

# **kwargs
def print_info(**details):  # details will be a dictionary
    for key, value in details.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```
- **Where to find examples**: Coming Soon.

### Lambda Functions
- **What they are**: Small, anonymous (unnamed) functions defined with the `lambda` keyword. They are restricted to a single expression.
- **How they work**: Syntax: `lambda arguments: expression`. The expression is evaluated and returned. Often used for short functions that are needed for a specific, limited purpose (e.g., as arguments to higher-order functions like `map`, `filter`, `sorted`).
- **Example**:
```python
# Anonymous function
double = lambda x: x * 2
print(double(5))  # Output: 10

# Used with sorted
points = [(1, 2), (3, 1), (5, 4)]
points.sort(key=lambda point: point[1]) # Sort by the second element of each tuple
print(points)  # Output: [(3, 1), (1, 2), (5, 4)]
```
- **Where to find examples**: Coming Soon.

## Functional Programming

### Map
- **What it is**: A built-in function that applies a given function to each item of an iterable (like a list or tuple) and returns a map object (an iterator) containing the results.
- **How it works**: `map(function, iterable1, iterable2, ...)`
- **Example**:
```python
numbers = [1, 2, 3, 4]
# Using a lambda function with map
doubled_iterator = map(lambda x: x * 2, numbers)
doubled_list = list(doubled_iterator)  # Convert iterator to list: [2, 4, 6, 8]
print(doubled_list)
```
- **Where to find examples**: Coming Soon.

### Filter
- **What it is**: A built-in function that constructs an iterator from elements of an iterable for which a function returns true.
- **How it works**: `filter(function, iterable)`. The `function` should return a boolean value.
- **Example**:
```python
numbers = [1, 2, 3, 4, 5, 6]
# Using a lambda function with filter
evens_iterator = filter(lambda x: x % 2 == 0, numbers)
evens_list = list(evens_iterator)  # Convert iterator to list: [2, 4, 6]
print(evens_list)
```
- **Where to find examples**: Coming Soon.

### Reduce
- **What it is**: A function (found in the `functools` module) that applies a rolling computation to sequential pairs of values in an iterable, reducing the iterable to a single accumulated result.
- **How it works**: `reduce(function, iterable[, initializer])`. The `function` takes two arguments (accumulator, current_element). `initializer` is an optional starting value for the accumulator.
- **Example**:
```python
from functools import reduce
numbers = [1, 2, 3, 4]
# Using a lambda function with reduce to find the product
product = reduce(lambda x, y: x * y, numbers)  # ( ( (1*2)*3 )*4 ) = 24
print(product)

# With an initializer
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10) # 10+1+2+3+4 = 20
print(sum_with_initial)
```
- **Where to find examples**: Coming Soon.

## File Operations

### Reading Files
- **What it is**: Interacting with files stored on the computer's file system to retrieve their content.
- **How it works**:
    - Use the `open()` function, typically with a `with` statement (context manager) to ensure the file is automatically closed.
    - Modes for reading: `'r'` (text mode, default), `'rb'` (binary mode).
    - Methods:
        - `file.read()`: Reads the entire file content.
        - `file.readline()`: Reads a single line.
        - `file.readlines()`: Reads all lines into a list of strings.
        - Iterating over the file object directly reads line by line.
- **Example**:
```python
# Basic file reading (assuming 'example.txt' exists)
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# Reading line by line
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line.strip()) # .strip() removes leading/trailing whitespace
```
- **Where to find examples**: Coming Soon.

### Writing Files
- **What it is**: Creating new files or modifying existing ones on the file system.
- **How it works**:
    - Use `open()` with a `with` statement.
    - Modes for writing:
        - `'w'` (write mode): Overwrites the file if it exists, creates it if not.
        - `'a'` (append mode): Adds content to the end of the file if it exists, creates it if not.
        - `'wb'`, `'ab'` for binary writing/appending.
    - Methods:
        - `file.write(string)`: Writes a string to the file.
        - `file.writelines(list_of_strings)`: Writes a list of strings to the file.
- **Example**:
```python
# Writing to file (will create or overwrite 'output.txt')
# with open('output.txt', 'w') as file:
#     file.write("Hello, World!\n")
#     file.write("This is a new line.")

# Appending to a file
# with open('output.txt', 'a') as file:
#     file.write("\nAppending more text.")
```
- **Where to find examples**: Coming Soon.

## Modules and Imports

### Basic Import
- **What it is**: Modules are Python files (`.py`) containing definitions and statements (functions, classes, variables). Importing allows you to use these definitions in other Python files or interactive sessions, promoting code organization and reusability.
- **How it works**: `import module_name`. After importing, you access items from the module using dot notation: `module_name.item_name`.
- **Example**:
```python
import math  # Imports the built-in math module
result = math.sqrt(16)  # Accesses the sqrt function from the math module
print(result)           # Output: 4.0
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `import re`, `import secrets`, `import string`)

### Import Specific Items
- **What it is**: Importing specific names (functions, classes, variables) from a module directly into the current namespace. This means you can use them without prefixing them with the module name.
- **How it works**: `from module_name import item_name1, item_name2`.
- **Example**:
```python
from math import sqrt, pi  # Imports only sqrt and pi from math
result = sqrt(16)          # Used directly, no math. prefix
print(result)              # Output: 4.0
print(pi)                  # Output: 3.141592653589793
```
- **Where to find examples**: Coming Soon. (Though `Pasword_Generator.py` uses full module imports)

### Import with Alias
- **What it is**: Importing a module or specific items from a module and giving them a different name (an alias) in the current namespace. Useful for brevity or to avoid naming conflicts.
- **How it works**:
    - `import module_name as alias_name`
    - `from module_name import item_name as alias_name`
- **Example**:
```python
import numpy as np  # Common alias for the numpy library
# array = np.array([1, 2, 3]) # Now use np instead of numpy

from math import factorial as fact
print(fact(5))  # Output: 120
```
- **Where to find examples**: Coming Soon.

## Error Handling

### Try-Except
- **What it is**: A mechanism to gracefully handle runtime errors (exceptions) that might occur during program execution, preventing the program from crashing.
- **How it works**:
    - `try` block: Contains the code that might raise an exception.
    - `except ExceptionType:` block: If an exception of `ExceptionType` occurs in the `try` block, the code in this `except` block is executed. If `ExceptionType` is omitted, it catches any exception (generally not recommended for broad catches).
- **Example**:
```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
# Program continues instead of crashing
```
- **Where to find examples**: Coming Soon.

### Multiple Exceptions
- **What it is**: Handling different types of exceptions in different ways, or handling multiple specific exceptions with the same block of code.
- **How it works**:
    - Multiple `except` blocks: Each handles a specific exception type.
    - Tuple of exceptions: `except (TypeError, ValueError):` handles either `TypeError` or `ValueError`.
    - `except Exception as e:`: Catches any exception (subclass of `Exception`) and assigns the exception object to `e`, allowing you to inspect the error.
    - `else` block: (Optional) Executes if the `try` block completes without raising any exceptions.
    - `finally` block: (Optional) Always executes, regardless of whether an exception occurred or was handled. Useful for cleanup operations (e.g., closing files).
- **Example**:
```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("Invalid input: Please enter a whole number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result is: {result}")
finally:
    print("Execution finished or attempted.")
```
- **Where to find examples**: Coming Soon.

## Regular Expressions

### Basic Pattern Matching
- **What it is**: Regular expressions (regex or regexp) are sequences of characters that define a search pattern. They are a powerful tool for finding, matching, and manipulating text.
- **How it works**: Python's `re` module provides regex functionality.
    - `re.search(pattern, string)`: Scans the string for the first location where the pattern produces a match, and returns a match object if found, else `None`.
    - `re.match(pattern, string)`: Tries to apply the pattern at the start of the string. Returns a match object if found, else `None`.
    - `re.findall(pattern, string)`: Returns a list of all non-overlapping matches of the pattern in the string.
    - `re.sub(pattern, replacement, string)`: Replaces occurrences of the pattern in the string with `replacement`.
    - Match objects have methods like `group()` to retrieve the matched text.
    - It's common to use raw strings (e.g., `r'\d+'`) for regex patterns to avoid issues with backslashes.
- **Example**:
```python
import re
text = "My phone number is 123-456-7890, not 987-654-3210."
pattern = r'\d{3}-\d{3}-\d{4}'  # Matches XXX-XXX-XXXX phone number format

match = re.search(pattern, text)
if match:
    print("First match found:", match.group())  # Found: 123-456-7890

all_matches = re.findall(pattern, text)
print("All matches:", all_matches)  # All matches: ['123-456-7890', '987-654-3210']
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `re.findall(pattern, password)`)

### Common Patterns
- **What they are**: Special characters and sequences used in regex to define patterns.
- **How they work**:
    - `\d`: Matches any digit (0-9). Equivalent to `[0-9]`.
    - `\D`: Matches any non-digit.
    - `\w`: Matches any alphanumeric character (letters, numbers, and underscore). Equivalent to `[a-zA-Z0-9_]`.
    - `\W`: Matches any non-alphanumeric character.
    - `\s`: Matches any whitespace character (space, tab, newline, etc.).
    - `\S`: Matches any non-whitespace character.
    - `.` : Matches any character except a newline (unless DOTALL flag is specified).
    - `[abc]`: Matches 'a', 'b', or 'c'. (Character set)
    - `[^abc]`: Matches any character except 'a', 'b', or 'c'.
    - `[a-z]`: Matches any lowercase letter from 'a' to 'z'.
    - `^`: Matches the start of the string (or start of a line in multiline mode).
    - `$`: Matches the end of the string (or end of a line in multiline mode).
    - `*`: Matches the preceding element zero or more times.
    - `+`: Matches the preceding element one or more times.
    - `?`: Matches the preceding element zero or one time.
    - `{n}`: Matches the preceding element exactly `n` times.
    - `{n,}`: Matches the preceding element `n` or more times.
    - `{n,m}`: Matches the preceding element between `n` and `m` times.
    - `|`: Acts as an OR operator (e.g., `cat|dog` matches "cat" or "dog").
    - `()`: Groups expressions and captures the matched text.
- **Example**:
```python
import re
# Match any digit
digit_pattern = r'\d'
# Match any letter (uppercase or lowercase)
letter_pattern = r'[a-zA-Z]'
# Match any whitespace
space_pattern = r'\s'
# Match email address (simplified example)
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
text_to_search = "Email me at test.user@example.com or call 12345."
emails_found = re.findall(email_pattern, text_to_search)
print(f"Emails: {emails_found}") # Emails: ['test.user@example.com']
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `r'\d'`, `r'[A-Z]'`, `r'[a-z]'`, `fr'[{symbols}]'`)

## Algorithms

### Searching
- **What it is**: The process of finding a specific item (target) within a collection of items (like a list or array).
- **How they work**:
    - **Linear Search**: Iterates through the collection one by one, comparing each item with the target until a match is found or the end of the collection is reached. Simple but can be inefficient for large collections (Time complexity: O(n)).
    - **Binary Search**: Efficiently finds a target in a **sorted** collection by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. (Time complexity: O(log n)).
- **Example**:
```python
# Linear search
def linear_search(arr, target):
    for i, item in enumerate(arr): # enumerate gives index and item
        if item == target:
            return i  # Return index of target
    return -1         # Target not found

# Binary search (requires arr to be sorted)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Integer division
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
- **Where to find examples**: Coming Soon.

### Sorting
- **What it is**: Arranging items in a collection in a specific order (e.g., ascending or descending).
- **How they work**:
    - **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. Simple to understand but inefficient for large lists (Time complexity: O(n^2)).
    - Many other sorting algorithms exist, like Merge Sort, Quick Sort (often more efficient, O(n log n) on average), Insertion Sort, etc. Python's built-in `sort()` method and `sorted()` function typically use Timsort, which is a hybrid stable sorting algorithm, derived from merge sort and insertion sort.
- **Example**:
```python
# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap
                swapped = True
        if not swapped: # If no two elements were swapped by inner loop, then break
            break
    return arr

my_numbers = [64, 34, 25, 12, 22, 11, 90]
# Using built-in sort
# my_numbers.sort() # Sorts in-place
# print(my_numbers)
# sorted_numbers = sorted(my_numbers) # Returns a new sorted list
# print(sorted_numbers)
```
- **Where to find examples**: Coming Soon.

## Project-Specific Concepts

### Password Generation
- **What it is**: Creating strong, random passwords that meet specific criteria (length, character types).
- **How it works**:
    - **Secure Randomness**: Uses the `secrets` module for generating cryptographically strong random numbers, suitable for passwords and security tokens, as opposed to the `random` module which is fine for modeling and simulation but not for security.
    - **Character Sets**: Defines pools of characters (lowercase, uppercase, digits, symbols) from the `string` module.
    - **Constraint Enforcement**: Generates passwords iteratively until all specified constraints (minimum number of each character type) are met.
    - **Validation**: Uses regular expressions (`re` module) to count occurrences of different character types in the generated password.
- **Where to find examples**: `Pasword_Generator.py`

### Cryptography (Vigenere Cipher)
- **What it is**: A method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It's a form of polyalphabetic substitution.
- **How it works**:
    - **Key**: A keyword is used. For example, if the keyword is "LEMON".
    - **Character Shifting**: Each letter in the plaintext is shifted by a certain amount based on the corresponding letter in the keyword. The keyword is repeated if it's shorter than the plaintext.
    - **Modular Arithmetic**: Used to wrap around the alphabet. For example, if shifting 'Y' by 3 letters in a 26-letter alphabet, the result is 'B'. `(index_of_char + index_of_key_char) % 26`.
    - **Decryption**: Involves shifting in the opposite direction: `(index_of_cipher_char - index_of_key_char + 26) % 26`.
- **Where to find examples**: Coming Soon.

### Credit Card Validation (Luhn Algorithm)
- **What it is**: A checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, etc. It's designed to protect against accidental errors (e.g., typos), not malicious attacks.
- **How it works**:
    1.  From the rightmost digit (check digit), double the value of every second digit.
    2.  If doubling a digit results in a two-digit number, subtract 9 from it (or, equivalently, add the two digits together: e.g., 14 becomes 1+4=5).
    3.  Sum all the resulting digits (including the undoubled digits).
    4.  If the total sum modulo 10 is equal to 0, the number is valid according to the Luhn formula.
- **Where to find examples**: Coming Soon.

### Numerical Methods (Bisection Method)
- **What it is**: A root-finding algorithm that repeatedly bisects an interval and then selects a subinterval in which a root must lie for further processing. It's a simple and robust method but can be relatively slow.
- **How it works**:
    - **Precondition**: Requires an initial interval `[a, b]` where the function `f(x)` is continuous and `f(a)` and `f(b)` have opposite signs (meaning, by the Intermediate Value Theorem, a root exists in `[a, b]`).
    - **Iteration**:
        1.  Calculate the midpoint `c = (a + b) / 2`.
        2.  Evaluate `f(c)`.
        3.  If `f(c)` is (close enough to) zero, `c` is the root.
        4.  If `f(a)` and `f(c)` have opposite signs, the root lies in `[a, c]`. Set `b = c`.
        5.  Else (if `f(c)` and `f(b)` have opposite signs), the root lies in `[c, b]`. Set `a = c`.
    - **Convergence**: Repeat until the interval is sufficiently small or a maximum number of iterations is reached.
- **Where to find examples**: Coming Soon.

### Data Processing (Expense Tracker)
- **What it is**: Managing and analyzing financial expense data.
- **How it works**:
    - **Data Storage**: Often uses lists of dictionaries or custom objects to store expense records (e.g., `[{'date': '2023-01-15', 'category': 'Food', 'amount': 25.50}, ...]`).
    - **CRUD Operations**: Implementing functions to Create, Read, Update, and Delete expense entries.
    - **Functional Programming**: May use `map`, `filter`, `reduce` for data transformations (e.g., filtering expenses by category, calculating total expenses).
    - **Reporting**: Generating summaries, like total expenses per category or over a time period.
    - **Command-Line Interface (CLI)**: Interacting with the user via text commands to manage expenses.
- **Where to find examples**: Coming Soon.

### Text Processing (Case Conversion)
- **What it is**: Manipulating text strings to change the case of characters (e.g., to uppercase, lowercase, title case).
- **How it works**:
    - **String Methods**: Python's built-in string methods are primarily used:
        - `text.lower()`: Converts all characters to lowercase.
        - `text.upper()`: Converts all characters to uppercase.
        - `text.title()`: Converts the first character of each word to uppercase and the rest to lowercase.
        - `text.capitalize()`: Converts the first character of the string to uppercase and the rest to lowercase.
        - `text.swapcase()`: Converts lowercase to uppercase and vice-versa.
    - **Regular Expressions**: Can be used for more complex case conversion patterns or conditional casing.
    - **List Comprehensions/Loops**: For applying case conversions to elements in a list of strings or parts of a string.
- **Where to find examples**: Coming Soon.

This cheat sheet covers the main Python concepts used throughout the repository's projects. Each project demonstrates different aspects of scientific computing and Python programming. It will be updated as more projects are added.
