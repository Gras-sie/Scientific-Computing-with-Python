# Scientific Computing with Python - Comprehensive Cheat Sheet

This repository contains various Python projects demonstrating scientific computing concepts. Below is a comprehensive cheat sheet covering all Python concepts used throughout the codebase, with detailed explanations and references to example files.

## Table of Contents
- [Basic Python Concepts](#basic-python-concepts)
  - [Variables](#variables)
  - [Data Types](#data-types)
  - [Operators](#operators)
  - [Type Conversion](#type-conversion)
  - [Input/Output](#inputoutput)
- [Data Structures](#data-structures)
  - [Lists](#lists)
  - [List Comprehensions](#list-comprehensions)
  - [Tuples](#tuples)
  - [Dictionaries](#dictionaries)
  - [Dictionary Comprehensions](#dictionary-comprehensions)
  - [Sets](#sets)
  - [Set Comprehensions](#set-comprehensions)
  - [Strings (as sequences)](#strings-as-sequences)
- [String Operations](#string-operations)
  - [String Methods](#string-methods)
  - [String Formatting](#string-formatting)
  - [String Slicing](#string-slicing)
  - [Raw Strings](#raw-strings)
  - [Multiline Strings](#multiline-strings)
- [Control Flow](#control-flow)
  - [Conditionals](#conditionals)
  - [Loops](#loops)
  - [The `pass` statement](#the-pass-statement)
  - [The `del` statement](#the-del-statement)
- [Functions](#functions)
  - [Basic Functions](#basic-functions)
  - [Parameters and Arguments](#parameters-and-arguments)
  - [Default Parameters](#default-parameters)
  - [Keyword Arguments](#keyword-arguments)
  - [*args and **kwargs](#args-and-kwargs)
  - [Scope (LEGB Rule)](#scope-legb-rule)
  - [Lambda Functions](#lambda-functions)
  - [Docstrings](#docstrings)
  - [Type Hinting](#type-hinting)
  - [Recursion](#recursion)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
  - [Classes and Objects](#classes-and-objects)
  - [Constructors (`__init__`)](#constructors-__init__)
  - [Instance Attributes](#instance-attributes)
  - [Class Attributes](#class-attributes)
  - [Methods (Instance, Class, Static)](#methods-instance-class-static)
  - [Inheritance](#inheritance)
  - [Polymorphism](#polymorphism)
  - [Encapsulation (Public, Protected, Private)](#encapsulation-public-protected-private)
  - [Special Methods (Dunder Methods)](#special-methods-dunder-methods)
  - [Properties (`@property`)](#properties-property)
- [Modules and Packages](#modules-and-packages)
  - [Basic Import](#basic-import)
  - [Import Specific Items](#import-specific-items)
  - [Import with Alias](#import-with-alias)
  - [Creating Modules](#creating-modules)
  - [Creating Packages](#creating-packages)
  - [The `if __name__ == "__main__":` block](#the-if-__name__--__main__-block)
- [Error Handling (Exceptions)](#error-handling-exceptions)
  - [Try-Except](#try-except)
  - [Handling Multiple Exceptions](#handling-multiple-exceptions)
  - [The `else` clause in try-except](#the-else-clause-in-try-except)
  - [The `finally` clause](#the-finally-clause)
  - [Raising Exceptions](#raising-exceptions)
  - [Custom Exceptions](#custom-exceptions)
- [File Operations](#file-operations)
  - [Opening and Closing Files (`with` statement)](#opening-and-closing-files-with-statement)
  - [Reading Files](#reading-files)
  - [Writing Files](#writing-files)
  - [File Modes](#file-modes)
  - [Working with File Pointers (`seek`, `tell`)](#working-with-file-pointers-seek-tell)
- [Iterators and Generators](#iterators-and-generators)
  - [Iterables and Iterators](#iterables-and-iterators)
  - [Generators (using `yield`)](#generators-using-yield)
  - [Generator Expressions](#generator-expressions)
- [Decorators](#decorators)
- [Context Managers](#context-managers)
- [Regular Expressions](#regular-expressions)
  - [Basic Pattern Matching](#basic-pattern-matching)
  - [Common Patterns and Metacharacters](#common-patterns-and-metacharacters)
  - [Match Object](#match-object)
  - [Compilation Flags](#compilation-flags)
- [Standard Library Highlights](#standard-library-highlights)
  - [`collections`](#collections-module)
  - [`datetime`](#datetime-module)
  - [`json`](#json-module)
  - [`os`](#os-module)
  - [`sys`](#sys-module)
  - [`math`](#math-module)
  - [`random`](#random-module)
  - [`itertools`](#itertools-module)
- [Virtual Environments](#virtual-environments)
- [The Walrus Operator (`:=`)](#the-walrus-operator-)
- [Algorithms](#algorithms)
  - [Searching](#searching)
  - [Sorting](#sorting)
- [Project-Specific Concepts](#project-specific-concepts)
  - [Password Generation](#password-generation)
  - [Cryptography (Vigenere Cipher)](#cryptography-vigenere-cipher)
  - [Credit Card Validation (Luhn Algorithm)](#credit-card-validation-luhn-algorithm)
  - [Numerical Methods (Bisection Method)](#numerical-methods-bisection-method)
  - [Data Processing (Expense Tracker)](#data-processing-expense-tracker)
  - [Text Processing (Case Conversion)](#text-processing-case-conversion)
  - [Shortest Path Algorithm](#shortest-path-algorithm)


## Basic Python Concepts

### Variables
- **What they are**: Variables are named references to memory locations where data values are stored. Python is dynamically typed, meaning you don't need to declare a variable's type; it's inferred at runtime.
- **How they work**: You assign a value to a variable using the assignment operator (`=`). Python handles memory allocation automatically. It's a convention (PEP 8) to use `snake_case` for variable names (e.g., `my_variable`).
- **Example**:
```python
my_variable = 42  # Integer
name = "John"     # String
is_valid = True   # Boolean
PI = 3.14159      # Convention for constants (still mutable)
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `letters`, `digits`, `password`)

### Data Types
- **What they are**: Fundamental categories of data. Python has several built-in data types.
    - **Numeric Types**:
        - **Integers (`int`)**: Whole numbers of arbitrary precision, positive or negative (e.g., `42`, `-7`, `10**100`).
        - **Floats (`float`)**: Numbers with a decimal point, representing real numbers (e.g., `3.14`, `-0.001`, `2.0e3`). Implemented as IEEE 754 double-precision.
        - **Complex Numbers (`complex`)**: Numbers with a real and imaginary part (e.g., `3+5j`, `2-1j`). The imaginary part is denoted by `j` or `J`.
    - **Sequences (Ordered)**:
        - **Strings (`str`)**: Immutable sequences of Unicode characters (e.g., `"Hello"`, `'World'`).
        - **Lists (`list`)**: Mutable (changeable) ordered sequences of items (e.g., `[1, "apple", True]`).
        - **Tuples (`tuple`)**: Immutable ordered sequences of items (e.g., `(1, "apple", True)`).
    - **Mappings (Unordered Key-Value)**:
        - **Dictionaries (`dict`)**: Mutable collections of key-value pairs (e.g., `{"name": "Alice", "age": 30}`). Keys must be unique and hashable. Ordered as of Python 3.7+.
    - **Sets (Unordered Collections of Unique Items)**:
        - **Sets (`set`)**: Mutable collections of unique, hashable items (e.g., `{1, 2, 3}`).
        - **Frozen Sets (`frozenset`)**: Immutable versions of sets.
    - **Booleans (`bool`)**: Represent truth values, `True` or `False`. Subclass of `int` where `True` is 1 and `False` is 0.
    - **None (`NoneType`)**: Represents the absence of a value or a null value. It's a unique object.
- **How they work**: Python automatically determines the data type when you assign a value. You can check the type of a variable using `type(variable)`.
- **Example**:
```python
integer_num = 100
float_num = 3.14
complex_num = 2 + 3j
my_string = "Python"
my_list_example = [1, 2, "a"]
my_tuple_example = (1, 2, "a")
my_dict_example = {"key": "value"}
my_set_example = {1, 2, 2, 3} # {1, 2, 3}
is_active = False
nothing = None

print(type(integer_num))  # <class 'int'>
print(type(my_string))    # <class 'str'>
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., string literals, integer parameters)

### Operators
- **What they are**: Special symbols or keywords that perform operations on operands (values or variables).
- **How they work**:
    - **Arithmetic Operators**: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (true division), `//` (floor division), `%` (modulus), `**` (exponentiation).
    - **Comparison (Relational) Operators**: `==` (equal to), `!=` (not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to). Return `True` or `False`.
    - **Logical Operators**: `and` (logical AND), `or` (logical OR), `not` (logical NOT).
    - **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `>>=`, `<<=`.
    - **Bitwise Operators**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift).
    - **Identity Operators**: `is` (true if operands are the same object), `is not` (true if operands are not the same object).
    - **Membership Operators**: `in` (true if value is found in sequence), `not in` (true if value is not found in sequence).
- **Example**:
```python
a = 10
b = 3
print(a + b)    # 13
print(a / b)    # 3.333...
print(a // b)   # 3 (floor division)
print(a % b)    # 1 (modulus)
print(a > b)    # True
print(a == 10 and b < 5) # True

c = [1, 2, 3]
d = c
e = [1, 2, 3]
print(d is c)   # True (d and c point to the same object)
print(e is c)   # False (e is a different object, even with same content)
print(e == c)   # True (contents are the same)
print(1 in c)   # True
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `+` for string concatenation, `<=` for comparison)

### Type Conversion
- **What it is**: Explicitly changing an object from one data type to another. Also known as type casting.
- **How they work**: Python provides built-in functions for type conversion.
    - `int(x)`: Converts `x` to an integer.
    - `float(x)`: Converts `x` to a floating-point number.
    - `str(x)`: Converts `x` to a string.
    - `list(x)`: Converts an iterable `x` to a list.
    - `tuple(x)`: Converts an iterable `x` to a tuple.
    - `set(x)`: Converts an iterable `x` to a set.
    - `dict(x)`: Converts `x` (e.g., a list of key-value tuples) to a dictionary.
    - `bool(x)`: Converts `x` to a Boolean value. Most values are `True`, except for `False`, `None`, numeric zero of all types, and empty sequences/mappings.
- **Example**:
```python
str_num = "42"
num = int(str_num)          # Convert string to integer (num is 42)
float_val = float("3.14")   # Convert string to float (float_val is 3.14)
num_str = str(123)          # Convert integer to string (num_str is "123")
my_tuple = (1, 2)
my_list_from_tuple = list(my_tuple) # [1, 2]
is_true = bool(1)           # Convert integer to boolean (True)
is_false = bool(0)          # Convert integer to boolean (False)
is_false_too = bool("")     # Convert empty string to boolean (False)
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `list(graph)` in `ShortestPath_Algorithm.py` if it were used there, `str()` implicitly in f-strings)

### Input/Output
- **What it is**: How a program interacts with the user or external sources.
- **How it works**:
    - **`print()` function**: Outputs data to the standard output (usually the console).
        - Can take multiple arguments, separated by commas.
        - `sep` argument: Specifies the separator between arguments (default is a space).
        - `end` argument: Specifies what to print at the end (default is a newline `\n`).
    - **`input()` function**: Reads a line of text from standard input (usually the keyboard).
        - Always returns the input as a string.
        - Can take an optional string argument as a prompt.
- **Example**:
```python
name = input("Enter your name: ")
print("Hello,", name, "!", sep="---", end="***\n") # Example: Hello,---Alice!---***

age_str = input("Enter your age: ")
try:
    age = int(age_str)
    print(f"You will be {age + 1} next year.")
except ValueError:
    print("Invalid age entered.")
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `print('Generated password:', new_password)`)

## Data Structures

### Lists
- **What they are**: Ordered, mutable (changeable) collections of items. Lists can contain items of different data types. They are one of the most versatile data structures in Python.
- **How they work**:
    - Defined using square brackets `[]`, with items separated by commas.
    - **Indexing**: Access items by their position (index), starting from 0. Negative indices count from the end (`-1` is the last item).
    - **Slicing**: Extract a sub-list using `my_list[start:stop:step]`. Slices create a new list (shallow copy).
    - **Mutability**: Items can be changed, added, or removed after creation.
    - **Common Methods**:
        - `append(item)`: Adds `item` to the end.
        - `extend(iterable)`: Appends all items from `iterable` to the end.
        - `insert(index, item)`: Inserts `item` at `index`.
        - `remove(item)`: Removes the first occurrence of `item`. Raises `ValueError` if not found.
        - `pop(index=-1)`: Removes and returns the item at `index` (default is the last item).
        - `clear()`: Removes all items.
        - `index(item, start=0, end=len(list))`: Returns the index of the first occurrence of `item`. Raises `ValueError` if not found.
        - `count(item)`: Returns the number of occurrences of `item`.
        - `sort(key=None, reverse=False)`: Sorts the list in-place.
        - `reverse()`: Reverses the list in-place.
        - `copy()`: Returns a shallow copy of the list (equivalent to `my_list[:]`).
- **Example**:
```python
my_list = [1, 2, 3, "hello", True]
print(my_list[0])      # Accesses 1
print(my_list[-1])     # Accesses True
my_list[1] = "world"   # Modify item: [1, "world", 3, "hello", True]
my_list.append(4)      # [1, "world", 3, "hello", True, 4]
my_list.insert(1, "new") # [1, "new", "world", 3, "hello", True, 4]
popped_item = my_list.pop() # popped_item is 4
print(my_list.index("world")) # 2
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(reverse=True) # [9, 5, 4, 3, 2, 1, 1]
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `constraints` list)

### List Comprehensions
- **What they are**: A concise and readable way to create lists. Often more efficient than using explicit `for` loops and `append`.
- **How they work**: The basic syntax is `[expression for item in iterable if condition]`.
    - `expression`: The value to be included in the new list.
    - `item`: Variable representing each element from the iterable.
    - `iterable`: The sequence or collection to iterate over.
    - `if condition` (optional): A filter that includes the item only if the condition is true.
- **Example**:
```python
squares = [x**2 for x in range(10)]  # Creates [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(10) if x % 2 == 0]  # Creates [0, 2, 4, 6, 8]
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words] # ['HELLO', 'WORLD', 'PYTHON']
# Nested list comprehension
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row] # [1, 2, 3, 4]
```
- **Where to find examples**: `ShortestPath_Algorithm.py` (e.g., `unvisited = list(graph)` is not a comprehension, but `distances = {node: 0 if node == start else float('inf') for node in graph}` is a dictionary comprehension).

### Tuples

- **What they are**: Ordered, immutable (unchangeable) sequences of items. Often used for fixed collections of items, for data that should not be modified, or as keys in dictionaries (since they are hashable if all their elements are hashable).
- **How they work**:
    - Defined using parentheses `()`, with items separated by commas. Parentheses are optional in many contexts if the commas make the tuple clear.
    - A tuple with a single element needs a trailing comma: `(1,)`.
    - **Indexing and Slicing**: Same as lists.
    - **Immutability**: Cannot be changed after creation. This means you cannot add, remove, or modify items.
    - **Tuple Packing and Unpacking**:
        - Packing: `my_tuple = 1, "a", True`
        - Unpacking: `x, y, z = my_tuple` (number of variables must match tuple length)
- **Example**:
```python
point = (10, 20, 30)      # Tuple packing
x, y, z = point          # Tuple unpacking (x=10, y=20, z=30)
# point[0] = 5       # This would raise a TypeError because tuples are immutable
single_item_tuple = ("hello",) # Note the trailing comma
empty_tuple = ()

# Tuples are often returned from functions that need to return multiple values
def get_coordinates():
    return 10, 20
lat, lon = get_coordinates()
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., items in the `constraints` list like `(nums, r'\d')`)

### Dictionaries
- **What they are**: Mutable collections of key-value pairs. Keys must be unique and hashable (immutable types like strings, numbers, or tuples containing only hashable types). Dictionaries are optimized for retrieving values when the key is known. As of Python 3.7, dictionaries maintain insertion order.
- **How they work**:
    - Defined using curly braces `{}`, with `key: value` items separated by commas, or using the `dict()` constructor.
    - **Accessing Values**: `my_dict[key]`. Raises `KeyError` if key is not found.
    - `my_dict.get(key, default_value)`: Safely gets a value; returns `default_value` (or `None`) if key is not found.
    - **Adding/Updating Items**: `my_dict[key] = value`.
    - **Removing Items**:
        - `del my_dict[key]`: Removes item by key. Raises `KeyError` if not found.
        - `my_dict.pop(key, default_value)`: Removes and returns value by key.
        - `my_dict.popitem()`: Removes and returns an arbitrary (key, value) pair (LIFO in Python 3.7+).
    - **Common Methods**:
        - `keys()`: Returns a view object displaying a list of all keys.
        - `values()`: Returns a view object displaying a list of all values.
        - `items()`: Returns a view object displaying a list of key-value tuple pairs.
        - `update(other_dict)`: Updates the dictionary with key-value pairs from `other_dict`.
        - `clear()`: Removes all items.
        - `copy()`: Returns a shallow copy.
- **Example**:
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])                 # Accesses "Alice"
person["email"] = "alice@example.com" # Adds a new key-value pair
person["age"] = 31                    # Updates the value for "age"
print(person.get("country", "USA"))   # "USA" (country key doesn't exist)

for key, value in person.items():
    print(f"{key}: {value}")

if "name" in person: # Check for key existence
    print("Name is present.")
```
- **Where to find examples**: `ShortestPath_Algorithm.py` (e.g., `my_graph`, `distances`, `paths`)

### Dictionary Comprehensions
- **What they are**: A concise way to create dictionaries.
- **How they work**: Syntax: `{key_expression: value_expression for item in iterable if condition}`.
- **Example**:
```python
numbers = [1, 2, 3, 4]
square_dict = {x: x**2 for x in numbers} # {1: 1, 2: 4, 3: 9, 4: 16}

words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words} # {'apple': 5, 'banana': 6, 'cherry': 6}
```
- **Where to find examples**: `ShortestPath_Algorithm.py` (e.g., `distances = {node: 0 if node == start else float('inf') for node in graph}`)

### Sets
- **What they are**: Mutable, unordered collections of unique, hashable items. Useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations like union, intersection, difference.
- **How they work**:
    - Defined using curly braces `{}` with items separated by commas, or using the `set()` constructor.
    - To create an empty set, you must use `set()`, as `{}` creates an empty dictionary.
    - Duplicates are automatically removed.
    - **Common Operations/Methods**:
        - `add(item)`: Adds an item.
        - `remove(item)`: Removes an item. Raises `KeyError` if not found.
        - `discard(item)`: Removes an item if present; does nothing otherwise.
        - `pop()`: Removes and returns an arbitrary item.
        - `clear()`: Removes all items.
        - `union(other_set)` or `|`: Returns a new set with elements from both sets.
        - `intersection(other_set)` or `&`: Returns a new set with elements common to both.
        - `difference(other_set)` or `-`: Returns a new set with elements in this set but not in `other_set`.
        - `symmetric_difference(other_set)` or `^`: Returns a new set with elements in either set, but not both.
        - `issubset(other_set)` or `<=`: Checks if this set is a subset of `other_set`.
        - `issuperset(other_set)` or `>=`: Checks if this set is a superset of `other_set`.
        - `isdisjoint(other_set)`: Checks if the two sets have no elements in common.
- **Example**:
```python
unique_numbers = {1, 2, 3, 3, 2, 4}  # Results in {1, 2, 3, 4}
empty_s = set()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)           # {1, 2, 3, 4, 5} (union)
print(set1 & set2)           # {3} (intersection)
print(set1 - set2)           # {1, 2} (difference)
set1.add(5)                  # {1, 2, 3, 5}
print(2 in set1)             # True
```
- **Where to find examples**: Coming Soon.

### Set Comprehensions
- **What they are**: A concise way to create sets.
- **How they work**: Syntax: `{expression for item in iterable if condition}`.
- **Example**:
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers} # {1, 4, 9, 16, 25}
```
- **Where to find examples**: Coming Soon.

### Strings (as sequences)
- While covered under Data Types and String Operations, it's important to remember strings are immutable sequences of characters. This means they support indexing, slicing, and iteration like lists and tuples.
- **Example**:
```python
my_str = "Python"
print(my_str[0])    # 'P'
print(my_str[1:4])  # 'yth'
for char in my_str:
    print(char)
# my_str[0] = 'J' # This would raise a TypeError
```
- **Where to find examples**: `Pasword_Generator.py`

## String Operations

### String Methods
- **What they are**: Built-in functions that operate on strings. Since strings are immutable, these methods return new strings rather than modifying the original.
- **How they work**: Called using dot notation on a string variable (e.g., `text.lower()`).
    - `.lower()`, `.upper()`: Convert case.
    - `.capitalize()`: First character uppercase, rest lowercase.
    - `.title()`: First character of each word uppercase.
    - `.swapcase()`: Swap case of all characters.
    - `.replace(old, new, count=-1)`: Replace occurrences of `old` with `new`. `count` limits replacements.
    - `.strip([chars])`, `.lstrip([chars])`, `.rstrip([chars])`: Remove leading/trailing whitespace or specified `chars`.
    - `.split(separator=None, maxsplit=-1)`: Split string into a list of substrings. If `separator` is not given, splits by whitespace and discards empty strings.
    - `.join(iterable)`: Join elements of an `iterable` (of strings) into a single string, using the string itself as a separator.
    - `.find(substring, start=0, end=len(string))`: Returns the lowest index of `substring` if found, else -1.
    - `.index(substring, start=0, end=len(string))`: Like `find()`, but raises `ValueError` if not found.
    - `.startswith(prefix, start=0, end=len(string))`, `.endswith(suffix, start=0, end=len(string))`: Check if string starts/ends with prefix/suffix.
    - `.count(substring, start=0, end=len(string))`: Returns number of non-overlapping occurrences.
    - `.isalpha()`, `.isdigit()`, `.isalnum()`, `.isspace()`, `.islower()`, `.isupper()`, `.istitle()`: Check character properties.
    - `.zfill(width)`: Pads string on the left with zeros to reach `width`.
    - `.center(width, fillchar=' ')`, `.ljust(width, fillchar=' ')`, `.rjust(width, fillchar=' ')`: Justify string.
- **Example**:
```python
text = "  Hello, World!  "
print(text.strip().upper().replace("WORLD", "PYTHON")) # "HELLO, PYTHON!"
words = "apple,banana,cherry".split(',') # ['apple', 'banana', 'cherry']
print("-".join(words))                   # "apple-banana-cherry"
print("filename.txt".endswith(".txt"))   # True
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `string.ascii_letters`, `string.digits`, `string.punctuation` are strings with useful properties, `join` in `ShortestPath_Algorithm.py`)

### String Formatting
- **What it is**: Creating strings by embedding expressions or variables within them.
- **How it works**:
    - **f-strings (Formatted String Literals, Python 3.6+)**: Prefix string with `f` or `F`. Expressions in `{}` are evaluated at runtime. Supports formatting specifiers (e.g., `{value:.2f}` for float with 2 decimal places). Most modern and preferred method.
    - **`str.format()` method**: Placeholders `{}` (numbered or named) are replaced by arguments to `.format()`. Also supports formatting specifiers.
    - **`%` operator (older C-style)**: Uses `%s`, `%d`, `%f` etc. as placeholders. Generally less flexible and readable than f-strings or `str.format()`.
- **Example**:
```python
name = "Alice"
age = 30
pi_val = 3.14159265

# f-strings
message_f = f"{name.upper()} is {age} years old. Pi is approx {pi_val:.3f}."
print(message_f) # ALICE is 30 years old. Pi is approx 3.142.

# str.format()
message_format = "{} is {} years old. Pi is approx {:.3f}.".format(name.upper(), age, pi_val)
print(message_format)
message_format_named = "{n} is {a} years old.".format(n=name, a=age)
print(message_format_named)

# % formatting
message_percent = "%s is %d years old. Pi is approx %.3f." % (name.upper(), age, pi_val)
print(message_percent)
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `fr'[{symbols}]'` in constraints, `print('Generated password:', new_password)`), `ShortestPath_Algorithm.py` (f-strings for printing paths).

### String Slicing
- **What it is**: Extracting a portion (substring) from a string. Slicing creates a new string.
- **How it works**: Uses the syntax `string[start:stop:step]`.
    - `start`: The starting index (inclusive). Defaults to 0 if omitted.
    - `stop`: The ending index (exclusive). Defaults to the end of the string if omitted.
    - `step`: The increment between indices. Defaults to 1 if omitted. Can be negative for reversing.
    - Negative indices count from the end of the string (`-1` is the last character).
- **Example**:
```python
text = "Hello, World!"
first_five = text[0:5]     # "Hello" (or text[:5])
world_part = text[7:12]    # "World"
from_end = text[-6:]       # "World!" (from 6th char from end to the end)
every_other = text[::2]    # "Hlo ol!" (every other character)
reversed_text = text[::-1] # "!dlroW ,olleH" (reversed string)
last_three = text[-3:]     # "ld!"
```
- **Where to find examples**: `ShortestPath_Algorithm.py` (e.g., `paths[current][:]` for list slicing, concept is similar for strings).

### Raw Strings
- **What they are**: String literals prefixed with `r` or `R`. In raw strings, backslashes are treated as literal characters and do not have special meaning (e.g., `\n` is not a newline, but two characters: `\` and `n`).
- **How they work**: Useful for regular expression patterns and Windows file paths where backslashes are common.
- **Example**:
```python
path = r"C:\Users\new_folder\notes.txt" # Backslashes are literal
print(path) # C:\Users\new_folder\notes.txt

regex_pattern = r"\d+\.\d+" # Matches one or more digits, a dot, one or more digits
print(regex_pattern) # \d+\.\d+
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `r'\d'` for regex patterns).

### Multiline Strings
- **What they are**: Strings that span multiple lines.
- **How they work**:
    - Using triple quotes (`"""..."""` or `'''...'''`). Newlines within the triple quotes are preserved in the string.
    - Using parentheses to group multiple string literals, which are implicitly concatenated. Newlines are not part of the string unless explicitly included with `\n`.
    - Using backslash `\` at the end of a line to continue the string on the next line (less common for multiline content, more for long single lines).
- **Example**:
```python
# Triple quotes
multiline_docstring = """This is a
multiline string that
preserves newlines."""
print(multiline_docstring)

# Implicit concatenation with parentheses
another_multiline = ("This is also a "
                     "multiline string, "
                     "but newlines are not included "
                     "unless specified with \\n.")
print(another_multiline)

# Backslash continuation (for a single logical line)
long_line = "This is a very long line that has been \
split over two physical lines for readability."
print(long_line)
```
- **Where to find examples**: Docstrings in all provided Python files.

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

### The `pass` statement
- **What it is**: A null operation. When the `pass` statement is executed, nothing happens.
- **How it works**: It's used as a placeholder when a statement is syntactically required, but you don't want any code to execute. This is common for stubs of functions or classes that you plan to implement later, or in conditional blocks where no action is needed for a particular case.
- **Example**:
```python
def my_function_stub():
    pass # TODO: Implement this later

class MyClass:
    pass # An empty class definition

value = 10
if value > 5:
    # Some logic here
    print("Value is greater than 5")
elif value == 5:
    pass # No specific action needed if value is 5
else:
    print("Value is less than 5")
```
- **Where to find examples**: Coming Soon.

### The `del` statement
- **What it is**: Used to remove a name binding (variable, item from a list, key from a dictionary, etc.) or to delete objects.
- **How it works**:
    - `del my_variable`: Removes the binding of `my_variable` from the current scope. If `my_variable` was the last reference to an object, the object may be garbage collected.
    - `del my_list[index]`: Deletes the item at `index` from `my_list`.
    - `del my_list[start:stop]`: Deletes a slice from `my_list`.
    - `del my_dict[key]`: Deletes the key-value pair associated with `key` from `my_dict`.
- **Example**:
```python
x = 100
print(x) # 100
del x
# print(x) # Would raise NameError: name 'x' is not defined

my_list_del = [10, 20, 30, 40, 50]
del my_list_del[1] # Deletes 20. my_list_del is now [10, 30, 40, 50]
del my_list_del[1:3] # Deletes 30, 40. my_list_del is now [10, 50]

my_dict_del = {'a': 1, 'b': 2, 'c': 3}
del my_dict_del['b'] # Deletes 'b': 2. my_dict_del is now {'a': 1, 'c': 3}
```
- **Where to find examples**: Coming Soon.

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

### Parameters and Arguments
- **What they are**:
    - **Parameters**: Names listed in a function's definition. They are placeholders for the values that will be passed to the function.
    - **Arguments**: The actual values that are passed to a function when it is called.
- **How they work**:
    - **Positional Arguments**: Passed to a function in the order they are defined. The first argument maps to the first parameter, and so on.
    - **Keyword Arguments**: Passed to a function by specifying the parameter name followed by an equals sign and the value (e.g., `func(param_name=value)`). The order of keyword arguments doesn't matter, as long as they come after any positional arguments.
- **Example**:
```python
def describe_pet(animal_type, pet_name): # animal_type and pet_name are parameters
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Positional arguments
describe_pet("hamster", "harry") # "hamster" is arg for animal_type, "harry" for pet_name

# Keyword arguments
describe_pet(animal_type="dog", pet_name="willie")
describe_pet(pet_name="lucy", animal_type="cat") # Order doesn't matter for keyword args

# Mixing positional and keyword (positional must come first)
describe_pet("bird", pet_name="tweetie")
# describe_pet(pet_name="goldie", "fish") # This would be a SyntaxError
```
- **Where to find examples**: All function definitions and calls.

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

### Keyword Arguments
- **What they are**: Arguments passed to a function call by explicitly naming the parameter they correspond to.
- **How they work**: `function_name(parameter_name=value)`. This improves readability and allows arguments to be passed out of positional order. All keyword arguments must follow any positional arguments in a function call.
- **Example**:
```python
def create_user(username, email, age, active=True):
    print(f"User: {username}, Email: {email}, Age: {age}, Active: {active}")

# Using keyword arguments for clarity and order flexibility
create_user(username="john_doe", email="john@example.com", age=30)
create_user(age=25, email="jane@example.com", username="jane_doe", active=False)
create_user("guest", email="guest@anon.com", age=99) # Mixing positional and keyword
```
- **Where to find examples**: `shortest_path(my_graph, 'A', target='F')` in `ShortestPath_Algorithm.py`.

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

### Scope (LEGB Rule)
- **What it is**: The region of a program where a particular name (variable, function) is accessible. Python uses the LEGB rule to resolve names:
    - **L (Local)**: Names assigned within a function (and not declared `global` or `nonlocal`). This is the innermost scope.
    - **E (Enclosing function locals)**: Names in the local scope of any and all enclosing functions (e.g., in nested functions), from inner to outer.
    - **G (Global)**: Names assigned at the top-level of a module file, or declared `global` in a function.
    - **B (Built-in)**: Names preassigned in Python (e.g., `print`, `len`, `Exception`).
- **How it works**: When a name is referenced, Python searches for it in these scopes in the LEGB order.
    - The `global` keyword can be used inside a function to indicate that an assignment should modify a global variable instead of creating a new local one.
    - The `nonlocal` keyword (Python 3+) can be used in nested functions to refer to a variable in an enclosing (but not global) scope.
- **Example**:
```python
x = "global x" # Global scope

def outer_func():
    y = "outer y" # Enclosing function local for inner_func

    def inner_func():
        z = "inner z" # Local scope
        print(z)      # Accesses local z
        print(y)      # Accesses enclosing y
        print(x)      # Accesses global x
        # print(len)  # Accesses built-in len
    inner_func()

outer_func()

count = 0 # Global
def increment_global():
    global count
    count += 1
increment_global()
print(count) # 1

def outer_nonlocal():
    level = "outer"
    def inner_nonlocal():
        nonlocal level
        level = "inner" # Modifies 'level' in outer_nonlocal's scope
        print(level)
    inner_nonlocal()
    print(level) # inner
outer_nonlocal()
```
- **Where to find examples**: Implicitly in all files. `my_graph` in `ShortestPath_Algorithm.py` is global.

### Docstrings
- **What they are**: String literals that appear as the first statement in a module, function, class, or method definition. They are used to document what the code does.
- **How they work**: Enclosed in triple quotes (`"""Docstring goes here"""` or `'''Docstring goes here'''`). They become the `__doc__` attribute of the object. Tools like Sphinx can automatically generate documentation from docstrings.
- **Conventions (e.g., PEP 257)**:
    - First line is a short summary.
    - Followed by a blank line, then a more detailed explanation if needed.
    - For functions/methods, often describe arguments, return values, and any exceptions raised.
- **Example**:
```python
def calculate_area(radius):
    """Calculate the area of a circle given its radius.

    Args:
        radius (float or int): The radius of the circle. Must be non-negative.

    Returns:
        float: The area of the circle.

    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    import math
    return math.pi * radius**2

print(calculate_area.__doc__)
# help(calculate_area) # Also displays the docstring
```
- **Where to find examples**: `Pasword_Generator.py` (function docstring), `ShortestPath_Algorithm.py` (module-level and function docstrings).

### Type Hinting
- **What it is**: (Python 3.5+) A way to statically indicate the expected types of variables, function parameters, and return values. Type hints are for documentation and can be used by static analysis tools (like MyPy) to catch type errors before runtime. Python itself does not enforce type hints at runtime by default.
- **How they work**:
    - For variables: `variable: type = value`
    - For function parameters: `def func(param: type): ...`
    - For function return values: `def func(...) -> return_type: ...`
    - The `typing` module provides more complex types (e.g., `List`, `Dict`, `Tuple`, `Optional`, `Union`, `Any`, `Callable`).
- **Example**:
```python
from typing import List, Optional, Dict

def greet_user(name: str) -> str:
    return f"Hello, {name}"

def process_numbers(numbers: List[int], factor: float = 1.0) -> List[float]:
    return [num * factor for num in numbers]

user_name: str = "Alice"
processed: List[float] = process_numbers([1, 2, 3], 0.5)

def get_item(data: Dict[str, int], key: str) -> Optional[int]:
    return data.get(key) # .get() returns None if key not found, matching Optional[int]
```
- **Where to find examples**: `shortest_path(graph, start, target = '')` in `ShortestPath_Algorithm.py` has a default parameter, which is a form of type information. Full type hints are not yet used.

### Recursion
- **What it is**: A programming technique where a function calls itself to solve a smaller instance of the same problem.
- **How it works**:
    - **Base Case**: A condition that stops the recursion (otherwise, it would loop infinitely).
    - **Recursive Step**: The part of the function where it calls itself with modified arguments, moving closer to the base case.
- **Common Examples**: Factorial, Fibonacci sequence, traversing tree-like data structures.
- **Caution**: Can lead to `RecursionError: maximum recursion depth exceeded` if the base case is not reached or the recursion is too deep. Iterative solutions are often more efficient in Python for simple cases due to function call overhead.
- **Example (Factorial)**:
```python
def factorial(n: int) -> int:
    """Calculates factorial of n recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1) # Recursive step

print(factorial(5)) # 120
```
- **Where to find examples**: Coming Soon.

## Object-Oriented Programming (OOP)
- **What it is**: A programming paradigm based on the concept of "objects", which can contain data in the form of fields (often known as attributes or properties) and code in the form of procedures (often known as methods). OOP aims to make code more modular, reusable, and easier to maintain.
- **Key Principles**:
    - **Encapsulation**: Bundling data (attributes) and methods that operate on that data within a single unit (object). Hiding internal state and requiring interaction through an object's public interface.
    - **Inheritance**: Creating new classes (derived or child classes) that inherit properties and methods from existing classes (base or parent classes). Promotes code reuse and establishes an "is-a" relationship.
    - **Polymorphism**: ("Many forms") The ability of an object to take on many forms. Commonly, it means that a call to a method will cause a different action depending on the type of object that invokes the method (e.g., different classes implementing the same method name).
    - **Abstraction**: Hiding complex implementation details and exposing only the essential features of an object or system.

### Classes and Objects
- **What they are**:
    - **Class**: A blueprint or template for creating objects. It defines a set of attributes and methods that the created objects will have.
    - **Object (Instance)**: A concrete instance of a class. You can create multiple objects from a single class.
- **How they work**:
    - Define a class using the `class` keyword.
    - Create an object (instantiate a class) by calling the class name as if it were a function.
- **Example**:
```python
class Dog:  # Class definition
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age): # Constructor method
        # Instance attributes (specific to each instance)
        self.name = name
        self.age = age

    def bark(self): # Instance method
        return "Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.name)        # Accessing instance attribute: Buddy
print(dog2.describe())  # Calling instance method: Lucy is 5 years old.
print(Dog.species)      # Accessing class attribute: Canis familiaris
print(dog1.species)     # Instances can also access class attributes
```
- **Where to find examples**: Coming Soon.

### Constructors (`__init__`)
- **What it is**: A special method in a class that is automatically called when an object of that class is created (instantiated). Its primary purpose is to initialize the instance's attributes.
- **How they work**: Named `__init__`. The first parameter is always `self`, which refers to the instance being created. Other parameters can be defined to accept arguments during instantiation.
- **Example**: (See `Dog` class example above)
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        print(f"A {year} {make} {model} has been created.")

my_car = Car("Toyota", "Camry", 2021) # __init__ is called here
```
- **Where to find examples**: Coming Soon.

### Instance Attributes
- **What they are**: Variables that belong to a specific instance of a class. Each object can have its own unique values for instance attributes.
- **How they work**: Typically defined within the `__init__` method using `self.attribute_name = value`. They are accessed using `instance.attribute_name`.
- **Example**: (In the `Dog` class, `self.name` and `self.age` are instance attributes)
```python
# ... (Dog class from above)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

dog1.color = "Brown" # You can also add instance attributes dynamically (generally less common)
print(dog1.name) # Buddy
print(dog2.name) # Lucy
print(dog1.color) # Brown
# print(dog2.color) # Would raise AttributeError, as dog2 doesn't have 'color'
```
- **Where to find examples**: Coming Soon.

### Class Attributes
- **What they are**: Variables that belong to the class itself, not to any particular instance. They are shared among all instances of the class.
- **How they work**: Defined directly within the class body, outside of any methods. Accessed using `ClassName.attribute_name` or `instance.attribute_name` (if not overridden by an instance attribute of the same name).
- **Example**: (In the `Dog` class, `species` is a class attribute)
```python
class Circle:
    pi = 3.14159 # Class attribute

    def __init__(self, radius):
        self.radius = radius # Instance attribute

    def area(self):
        return Circle.pi * (self.radius ** 2) # Accessing class attribute via class

c1 = Circle(5)
c2 = Circle(10)

print(c1.area())
print(c2.area())
print(Circle.pi) # 3.14159
print(c1.pi)     # 3.14159 (accessing through instance)

Circle.pi = 3.14 # Modifying class attribute affects all instances that haven't overridden it
print(c1.area()) # Uses the new value of pi

c1.pi = 3.14159265 # This creates an INSTANCE attribute 'pi' for c1, shadowing the class attribute
print(c1.pi)       # c1's own pi
print(c2.pi)       # c2 still uses Circle.pi (3.14)
print(Circle.pi)   # Circle.pi is still 3.14
```
- **Where to find examples**: Coming Soon.

### Methods (Instance, Class, Static)
- **What they are**: Functions defined within a class.
- **How they work**:
    - **Instance Methods**: The most common type. Operate on an instance of the class. The first parameter is always `self`, which refers to the instance calling the method.
        ```python
        class MyClass:
            def instance_method(self, arg1):
                print(f"Instance method called with {arg1} on {self}")
        obj = MyClass()
        obj.instance_method("hello")
        ```
    - **Class Methods**: Bound to the class and not the instance. The first parameter is `cls`, which refers to the class itself. They can modify class state (class attributes) or create instances of the class (e.g., factory methods). Decorated with `@classmethod`.
        ```python
        class MyClass:
            count = 0
            def __init__(self):
                MyClass.count += 1

            @classmethod
            def get_count(cls):
                return f"Number of instances: {cls.count}"

            @classmethod
            def from_string(cls, data_string):
                # Example factory method
                # name, age = data_string.split(',')
                # return cls(name, int(age)) # Assuming __init__ takes name and age
                pass
        obj1 = MyClass()
        obj2 = MyClass()
        print(MyClass.get_count()) # Number of instances: 2
        ```
    - **Static Methods**: Do not receive an implicit first argument (`self` or `cls`). They are like regular functions but belong to the class's namespace. They cannot modify object state or class state directly. Often utility functions that have some logical connection to the class. Decorated with `@staticmethod`.
        ```python
        class MathUtils:
            @staticmethod
            def add(x, y):
                return x + y

            @staticmethod
            def PI(): # No self or cls
                return 3.14159
        print(MathUtils.add(5, 3)) # 8
        print(MathUtils.PI())      # 3.14159
        ```
- **Where to find examples**: Coming Soon.

### Inheritance
- **What it is**: A mechanism where a new class (child/derived class) inherits attributes and methods from an existing class (parent/base class). This promotes code reuse and creates an "is-a" relationship (e.g., a `Dog` is an `Animal`).
- **How they work**:
    - Syntax: `class ChildClass(ParentClass): ...`
    - The child class can use (and override) methods from the parent class.
    - The `super()` function can be used in the child class to call methods of the parent class, especially useful in `__init__`.
    - Python supports multiple inheritance: `class Child(Parent1, Parent2): ...` (Method Resolution Order - MRO - determines which parent's method is called if there's a conflict).
- **Example**:
```python
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal created")

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal): # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name) # Call parent's __init__
        self.breed = breed
        print("Dog created")

    def speak(self): # Overriding parent's speak method
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        print("Cat created")

    def speak(self):
        return "Meow!"

my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Gray")

my_dog.eat()      # Inherited from Animal: Buddy is eating.
print(my_dog.speak()) # Overridden in Dog: Woof!
print(my_cat.speak()) # Overridden in Cat: Meow!
```
- **Where to find examples**: Coming Soon.

### Polymorphism
- **What it is**: ("Many forms") The ability of objects of different classes to respond to the same method call in a way specific to their class. This often involves a common interface (e.g., a method name) that different classes implement differently.
- **How it works**:
    - **Duck Typing**: "If it walks like a duck and quacks like a duck, then it must be a duck." Python focuses on an object's behavior (what methods it has) rather than its explicit type. If an object has the required method, it can be used polymorphically.
    - Achieved through method overriding (as seen in inheritance) or by different classes simply implementing methods with the same name.
- **Example**:
```python
# Using Dog and Cat classes from Inheritance example

def animal_sound(animal_object):
    # This function doesn't care if animal_object is Dog or Cat,
    # as long as it has a speak() method.
    print(animal_object.speak())

animal_sound(my_dog) # Woof!
animal_sound(my_cat) # Meow!

class Duck:
    def speak(self):
        return "Quack!"
    def swim(self):
        print("Duck is swimming")

my_duck = Duck()
animal_sound(my_duck) # Quack! (Duck typing in action)

# Another example: len() function works on various types
print(len("hello")) # 5 (string)
print(len([1, 2, 3])) # 3 (list)
print(len({"a":1, "b":2})) # 2 (dictionary)
```
- **Where to find examples**: Coming Soon.

### Encapsulation (Public, Protected, Private)
- **What it is**: Bundling data (attributes) and the methods that operate on that data within a single unit (an object). It also involves restricting direct access to some of an object's components, which is a way to prevent accidental modification of data.
- **How it works in Python (by convention)**:
    - **Public**: Attributes and methods accessible from anywhere. Default in Python.
        `self.name`
    - **Protected**: Attributes and methods intended for internal use within the class and its subclasses. Conventionally prefixed with a single underscore `_`. Python does not strictly enforce this; it's a hint to developers.
        `self._protected_member`
    - **Private**: Attributes and methods intended for internal use only within the class itself. Conventionally prefixed with a double underscore `__`. Python performs "name mangling" on these (e.g., `__private_member` becomes `_ClassName__private_member`), making them harder (but not impossible) to access directly from outside.
- **Example**:
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.public_holder = "Default Holder" # Public
        self._account_type = "Savings" # Protected convention
        self.__balance = initial_balance # Private (name mangled to _BankAccount__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__get_balance()}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__get_balance()}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def __get_balance(self): # "Private" helper method
        return self.__balance

    def _get_account_details(self): # "Protected" helper method
        return f"Type: {self._account_type}, Balance: {self.__balance}"

acc = BankAccount(100)
print(acc.public_holder)
# print(acc.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
print(acc._BankAccount__balance) # Can still be accessed via mangled name (not recommended)
acc.deposit(500)
# acc.__get_balance() # AttributeError
print(acc._get_account_details())
```
- **Where to find examples**: Coming Soon.

### Special Methods (Dunder Methods)
- **What they are**: Methods with double underscores at the beginning and end of their names (e.g., `__init__`, `__str__`, `__len__`). They allow you to define how objects of your class behave with built-in Python operations or functions.
- **How they work**: Python calls these methods automatically in specific situations.
- **Common Dunder Methods**:
    - `__init__(self, ...)`: Constructor, called when an object is created.
    - `__str__(self)`: Called by `str(object)` and `print(object)`. Should return a user-friendly string representation.
    - `__repr__(self)`: Called by `repr(object)`. Should return an unambiguous string representation, ideally one that could be used to recreate the object (`eval(repr(object)) == object`). If `__str__` is not defined, `__repr__` is used by `print`.
    - `__len__(self)`: Called by `len(object)`. Should return the "length" of the object.
    - `__getitem__(self, key)`: Called for `object[key]` (indexing).
    - `__setitem__(self, key, value)`: Called for `object[key] = value`.
    - `__delitem__(self, key)`: Called for `del object[key]`.
    - `__iter__(self)`: Called when an iterator is required for an object (e.g., in a `for` loop). Should return an iterator object.
    - `__next__(self)`: (For iterator objects) Returns the next item. Raises `StopIteration` when no more items.
    - `__call__(self, ...)`: Allows an instance of a class to be called as a function.
    - Comparison methods: `__eq__(self, other)` (for `==`), `__ne__(self, other)` (`!=`), `__lt__` (`<`), `__le__` (`<=`), `__gt__` (`>`), `__ge__` (`>=`).
    - Arithmetic methods: `__add__`, `__sub__`, `__mul__`, etc.
    - Context manager methods: `__enter__`, `__exit__`.
- **Example**:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): # For user-friendly output
        return f"Vector({self.x}, {self.y})"

    def __repr__(self): # For developer/debugging output
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other_vector): # Defines vector addition
        if isinstance(other_vector, Vector):
            return Vector(self.x + other_vector.x, self.y + other_vector.y)
        return NotImplemented # Important for other types

    def __len__(self):
        # Example: length could be number of dimensions
        return 2

v1 = Vector(2, 3)
v2 = Vector(5, 1)
print(str(v1)) # Vector(2, 3)
print(repr(v1))# Vector(x=2, y=3)
print(v1)      # Uses __str__ if available: Vector(2, 3)
v3 = v1 + v2   # Calls v1.__add__(v2)
print(v3)      # Vector(7, 4)
print(len(v1)) # 2
```
- **Where to find examples**: Coming Soon.

### Properties (`@property`)
- **What it is**: A way to create managed attributes. It allows you to define methods that are accessed like attributes (without parentheses), giving you control over getting, setting, and deleting an attribute's value.
- **How they work**:
    - Use the `@property` decorator for the getter method.
    - Use `@attribute_name.setter` for the setter method.
    - Use `@attribute_name.deleter` for the deleter method.
- **Benefits**:
    - Allows you to add logic (validation, computation) when an attribute is accessed or modified.
    - Provides a public interface while potentially having a different internal representation.
    - Can make an attribute read-only by defining only a getter.
- **Example**:
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius # "Protected" internal attribute

    @property
    def celsius(self): # Getter
        print("Getting Celsius value...")
        return self._celsius

    @celsius.setter
    def celsius(self, value): # Setter
        print("Setting Celsius value...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

    @property
    def fahrenheit(self): # Read-only computed property
        print("Calculating Fahrenheit...")
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)      # Calls getter: Getting Celsius value... 25
temp.celsius = 30        # Calls setter: Setting Celsius value...
print(temp.fahrenheit)     # Calls fahrenheit getter: Calculating Fahrenheit... 86.0
# temp.fahrenheit = 100  # AttributeError: can't set attribute (no setter for fahrenheit)
```
- **Where to find examples**: Coming Soon.

## Modules and Packages

### Basic Import
- **What it is**: Modules are Python files (`.py`) containing definitions and statements (functions, classes, variables). Importing allows you to use these definitions in other Python files or interactive sessions, promoting code organization and reusability.
- **How they work**: `import module_name`. After importing, you access items from the module using dot notation: `module_name.item_name`.
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

### Creating Modules
- **What it is**: Any Python file (`.py`) can be a module. Modules allow you to organize your code logically and reuse it in other programs.
- **How they work**:
    - Create a `.py` file (e.g., `my_module.py`).
    - Define functions, classes, and variables within it.
    - In another Python script (in the same directory, or a directory in `sys.path`), you can import it using `import my_module` or `from my_module import specific_item`.
- **Example** (`my_module.py`):
```python
# my_module.py
PI = 3.14159

def greet(name):
    return f"Hello, {name} from my_module!"

class MyClassInModule:
    def __init__(self, value):
        self.value = value
    def display(self):
        print(f"Value: {self.value}")
```
- **Example** (another script, `main.py`):
```python
# main.py
import my_module # Import the whole module

print(my_module.PI)
print(my_module.greet("Alice"))

obj = my_module.MyClassInModule(100)
obj.display()

from my_module import greet as greet_from_module # Import specific item with alias
print(greet_from_module("Bob"))
```
- **Where to find examples**: All `.py` files in the repository are modules.

### Creating Packages
- **What it is**: A way to structure Python's module namespace by using "dotted module names". A package is a collection of modules organized in a directory hierarchy.
- **How they work**:
    - A directory containing an `__init__.py` file is treated as a package. The `__init__.py` file can be empty, or it can execute initialization code for the package or set up the `__all__` variable (which defines what's imported with `from package import *`).
    - Modules within the package can be imported using dot notation (e.g., `import package_name.module_name` or `from package_name.module_name import item`).
- **Example Directory Structure**:
```
my_project/
├── main_app.py
└── my_package/
    ├── __init__.py
    ├── module1.py
    └── module2.py
    └── sub_package/
        ├── __init__.py
        └── module3.py
```
- **Example** (`my_package/__init__.py` - can be empty or):
```python
# my_package/__init__.py
print("my_package is being initialized")
from .module1 import func1 # Makes func1 available as my_package.func1
# __all__ = ["module1", "module2"] # For 'from my_package import *'
```
- **Example** (`my_package/module1.py`):
```python
# my_package/module1.py
def func1():
    print("Function 1 from module 1")
```
- **Example** (`main_app.py`):
```python
# main_app.py
import my_package.module1
my_package.module1.func1()

from my_package import module2 # Assuming module2.py exists
# print(module2.some_function_in_module2())

from my_package.sub_package import module3
# print(module3.another_function())

# If __init__.py did 'from .module1 import func1':
# import my_package
# print(my_package.func1())
```
- **Where to find examples**: The directory structure `Budget_App_Project/Regular_Expressions/` and `Budget_App_Project/Algorithm_Design/` implies packaging if `__init__.py` files were present.

### The `if __name__ == "__main__":` block
- **What it is**: A common Python idiom. The special variable `__name__` is set to `"__main__"` when a script is run directly. If the script is imported as a module into another script, `__name__` is set to the module's name.
- **How it works**: Code inside this block will only execute when the script is run directly, not when it's imported. This allows a module to provide reusable functions/classes and also have example code or tests that run only when the module file itself is executed.
- **Example** (`my_script.py`):
```python
# my_script.py
def useful_function():
    print("Useful function called.")

print(f"This script's __name__ is: {__name__}")

if __name__ == "__main__":
    print("This script is being run directly.")
    useful_function()
    # Example usage or tests for useful_function would go here
else:
    print("This script has been imported as a module.")

# If you run 'python my_script.py':
# Output:
# This script's __name__ is: __main__
# This script is being run directly.
# Useful function called.

# If another script does 'import my_script':
# Output (during import):
# This script's __name__ is: my_script
# This script has been imported as a module.
# (And then my_script.useful_function() can be called)
```
- **Where to find examples**: Not explicitly used in the provided files, but `Pasword_Generator.py` and `ShortestPath_Algorithm.py` have code at the bottom that runs when executed directly.

## Error Handling (Exceptions)

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

### Handling Multiple Exceptions
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

### Common Patterns and Metacharacters
- **What they are**: Special characters and sequences used in regex to define patterns.
- **How they work**:
    - `\d`: Matches any digit (0-9). Equivalent to `[0-9]`.
    - `\D`: Matches any non-digit.
    - `\w`: Matches any alphanumeric character (letters, numbers, and underscore). Equivalent to `[a-zA-Z0-9_]`.
    - `\W`: Matches any non-alphanumeric character.
    - `\s`: Matches any whitespace character (space, tab, newline, carriage return, form feed, vertical tab).
    - `\S`: Matches any non-whitespace character.
    - `.` : Matches any character except a newline (unless `re.DOTALL` flag is specified).
    - `[...]`: Character set. Matches any single character within the brackets.
        - `[abc]`: Matches 'a', 'b', or 'c'.
        - `[a-z]`: Matches any lowercase letter from 'a' to 'z'.
        - `[0-9]`: Matches any digit.
        - `[^abc]`: Negated set. Matches any character *not* in the brackets.
    - `^`: Matches the start of the string (or start of a line if `re.MULTILINE` is used).
    - `$`: Matches the end of the string (or end of a line if `re.MULTILINE` is used, before the newline).
    - `*`: Quantifier. Matches the preceding element zero or more times. Greedy.
    - `+`: Quantifier. Matches the preceding element one or more times. Greedy.
    - `?`: Quantifier. Matches the preceding element zero or one time. Greedy. Also used to make quantifiers non-greedy (`*?`, `+?`, `??`).
    - `{n}`: Quantifier. Matches the preceding element exactly `n` times.
    - `{n,}`: Quantifier. Matches the preceding element `n` or more times.
    - `{n,m}`: Quantifier. Matches the preceding element between `n` and `m` times (inclusive).
    - `|`: Alternation (OR operator). `cat|dog` matches "cat" or "dog".
    - `(...)`: Grouping. Creates a capturing group. The matched substring can be retrieved.
    - `(?:...)`: Non-capturing group. Groups expressions but doesn't save the matched part.
    - `(?P<name>...)`: Named capturing group.
    - `\b`: Word boundary. Matches the empty string at the beginning or end of a word.
    - `\B`: Non-word boundary.
    - Lookarounds (zero-width assertions):
        - `(?=...)`: Positive lookahead. Asserts that what follows matches `...`, but doesn't consume characters.
        - `(?!...)`: Negative lookahead. Asserts that what follows does *not* match `...`.
        - `(?<=...)`: Positive lookbehind. Asserts that what precedes matches `...`.
        - `(?<!...)`: Negative lookbehind. Asserts that what precedes does *not* match `...`.
- **Example**:
```python
import re
# Match email address (more robust example)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = "Contact us at support@example.com or sales.info@company.co.uk."
emails = re.findall(email_pattern, text) # ['support@example.com', 'sales.info@company.co.uk']

# Extracting parts of a date
date_text = "Date: 2023-10-26"
date_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_text)
if date_match:
    year, month, day = date_match.groups() # ('2023', '10', '26')
    print(f"Year: {year}, Month: {month}, Day: {day}")
```
- **Where to find examples**: `Pasword_Generator.py` (e.g., `r'\d'`, `r'[A-Z]'`, `r'[a-z]'`, `fr'[{symbols}]'`)

### Match Object
- **What it is**: An object returned by `re.search()` and `re.match()` (and `re.finditer()`) if a match is found. It contains information about the match.
- **How it works / Common Methods**:
    - `match.group(num=0)`: Returns the entire matched string, or a specific captured group if `num` > 0. `group()` is same as `group(0)`.
    - `match.groups()`: Returns a tuple containing all captured subgroups.
    - `match.groupdict()`: Returns a dictionary containing all named captured subgroups.
    - `match.start(group=0)`: Returns the starting index of the match (or a specific group).
    - `match.end(group=0)`: Returns the ending index of the match (or a specific group).
    - `match.span(group=0)`: Returns a tuple `(start, end)` of the match (or a specific group).
- **Example**:
```python
import re
text = "Name: Alice, Age: 30"
match = re.search(r"Name: (?P<name>\w+), Age: (?P<age>\d+)", text)
if match:
    print(f"Full match: {match.group(0)}")   # Name: Alice, Age: 30
    print(f"Name: {match.group('name')}")    # Alice (using named group)
    print(f"Age: {match.group(2)}")          # 30 (using group number)
    print(f"Groups tuple: {match.groups()}") # ('Alice', '30')
    print(f"Group dict: {match.groupdict()}")# {'name': 'Alice', 'age': '30'}
    print(f"Name starts at: {match.start('name')}") # 6
    print(f"Age ends at: {match.end('age')}")     # 20
```
- **Where to find examples**: `Pasword_Generator.py` (implicitly, as `re.findall` returns strings, but `re.search` would return match objects).

### Compilation Flags
- **What they are**: Flags that modify the behavior of regular expression matching.
- **How they work**: Can be passed as an argument to `re.compile()`, `re.search()`, `re.findall()`, etc., or embedded in the pattern using `(?flag)`.
    - `re.IGNORECASE` or `re.I`: Case-insensitive matching. `(?i)`
    - `re.MULTILINE` or `re.M`: `^` and `$` match the start/end of each line (not just the whole string). `(?m)`
    - `re.DOTALL` or `re.S`: `.` matches any character, *including* newlines. `(?s)`
    - `re.VERBOSE` or `re.X`: Allows you to write more readable regex by adding whitespace and comments. Whitespace is ignored, and `#` starts a comment. `(?x)`
    - `re.ASCII` or `re.A`: Makes `\w`, `\W`, `\b`, `\B`, `\s`, `\S` perform ASCII-only matching instead of full Unicode matching. `(?a)`
- **Example**:
```python
import re
text = "Hello\nworld"
# Case-insensitive
print(re.findall(r"hello", text, re.IGNORECASE)) # ['Hello']

# Multiline
print(re.findall(r"^\w+", text, re.MULTILINE)) # ['Hello', 'world']

# Verbose
pattern_verbose = re.compile(r"""
    \d+     # one or more digits
    \s+     # one or more whitespace characters
    \w+     # one or more word characters
""", re.VERBOSE)
print(pattern_verbose.findall("123 abc")) # ['123 abc'] (Note: findall returns full match for complex patterns)
```
- **Where to find examples**: Coming Soon.

## Standard Library Highlights
Python comes with a rich standard library. Here are a few commonly used modules:

### `collections` module
- Provides specialized container datatypes.
    - `defaultdict(default_factory)`: A subclass of `dict` that calls a factory function to supply missing values.
    - `Counter(iterable_or_mapping)`: A dict subclass for counting hashable objects.
    - `deque`: A list-like container with fast appends and pops from both ends (double-ended queue).
    - `namedtuple(typename, field_names)`: Factory function for creating tuple subclasses with named fields.
    - `OrderedDict`: (Less needed since Python 3.7+ as standard dicts are ordered). A dict subclass that remembers the order entries were added.
    - `ChainMap`: Groups multiple dicts or other mappings together to create a single, updateable view.
- **Example**:
```python
from collections import defaultdict, Counter, deque, namedtuple

# defaultdict
dd = defaultdict(int) # Default value for missing keys will be 0
dd['a'] += 1
print(dd['a']) # 1
print(dd['b']) # 0

# Counter
word_counts = Counter("abracadabra")
print(word_counts) # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(word_counts.most_common(2)) # [('a', 5), ('b', 2)]

# deque
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d) # deque([0, 1, 2, 3, 4])
d.popleft() # 0
print(d) # deque([1, 2, 3, 4])

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y) # 10 20
print(p[0])     # 10
```
- **Where to find examples**: Coming Soon.

### `datetime` module
- Supplies classes for manipulating dates and times.
    - `date`: Represents a date (year, month, day).
    - `time`: Represents a time (hour, minute, second, microsecond).
    - `datetime`: Represents a date and time.
    - `timedelta`: Represents a duration, the difference between two dates or times.
    - `timezone`: Represents timezone information.
- **Methods**: `now()`, `utcnow()`, `strptime()` (string to datetime), `strftime()` (datetime to string).
- **Example**:
```python
from datetime import datetime, timedelta, date

now = datetime.now()
print(f"Current datetime: {now}")
print(f"Current year: {now.year}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

today = date.today()
print(f"Today's date: {today}")

yesterday = today - timedelta(days=1)
print(f"Yesterday: {yesterday}")

date_str = "2023-01-15"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
print(f"Parsed date: {parsed_date}")
```
- **Where to find examples**: Coming Soon.

### `json` module
- For encoding Python objects as JSON strings and decoding JSON strings into Python objects.
    - `json.dumps(obj)`: Serialize `obj` to a JSON formatted `str`.
    - `json.loads(s)`: Deserialize `s` (a `str`, `bytes` or `bytearray` instance containing a JSON document) to a Python object.
    - `json.dump(obj, fp)`: Serialize `obj` as a JSON formatted stream to `fp` (a `.write()`-supporting file-like object).
    - `json.load(fp)`: Deserialize `fp` (a `.read()`-supporting file-like object containing a JSON document) to a Python object.
- **Example**:
```python
import json

data = {"name": "Alice", "age": 30, "isStudent": False, "courses": ["Math", "History"]}

# Python to JSON string
json_string = json.dumps(data, indent=4) # indent for pretty printing
print(json_string)

# JSON string to Python
parsed_data = json.loads(json_string)
print(parsed_data["name"]) # Alice

# Writing to a JSON file
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)

# Reading from a JSON file
# with open("data.json", "r") as f:
#     loaded_data_from_file = json.load(f)
#     print(loaded_data_from_file["courses"])
```
- **Where to find examples**: Coming Soon.

### `os` module
- Provides a way of using operating system dependent functionality like reading or writing to the file system, interacting with environment variables, process management, etc.
    - `os.getcwd()`: Get current working directory.
    - `os.chdir(path)`: Change current working directory.
    - `os.listdir(path='.')`: List directory contents.
    - `os.mkdir(path)`, `os.makedirs(path)`: Create directory/directories.
    - `os.remove(path)`, `os.rmdir(path)`: Remove file/empty directory.
    - `os.path.join(path, *paths)`: Join path components intelligently.
    - `os.path.exists(path)`, `os.path.isfile(path)`, `os.path.isdir(path)`: Check path properties.
    - `os.environ`: A dictionary representing environment variables.
    - `os.system(command)`: Execute a shell command (less secure, `subprocess` module is preferred).
- **Example**:
```python
import os

print(f"Current directory: {os.getcwd()}")
# os.mkdir("new_dir_example")
print(f"Files in current dir: {os.listdir('.')}")
filepath = os.path.join("my_folder", "my_file.txt") # Creates 'my_folder/my_file.txt' or 'my_folder\\my_file.txt'
print(f"Constructed path: {filepath}")
print(f"Does 'README.md' exist? {os.path.exists('README.md')}")
```
- **Where to find examples**: Coming Soon.

### `sys` module
- Provides access to system-specific parameters and functions.
    - `sys.argv`: List of command-line arguments passed to a Python script. `sys.argv[0]` is the script name.
    - `sys.exit(arg=0)`: Exit from Python. `arg` is the exit status (0 is success).
    - `sys.path`: A list of strings that specifies the search path for modules.
    - `sys.platform`: String identifying the platform (e.g., 'linux', 'win32', 'darwin').
    - `sys.version`: String containing the Python interpreter version.
    - `sys.stdin`, `sys.stdout`, `sys.stderr`: File objects for standard input, output, and error streams.
- **Example**:
```python
import sys

print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
# sys.exit("Exiting with a message.")
```
- **Where to find examples**: Coming Soon.

### `math` module
- Provides access to mathematical functions defined by the C standard.
    - `math.pi`, `math.e`
    - `math.sqrt(x)`: Square root.
    - `math.pow(x, y)`: `x` raised to the power `y`.
    - `math.sin(x)`, `math.cos(x)`, `math.tan(x)`: Trigonometric functions (x in radians).
    - `math.degrees(x)`, `math.radians(x)`: Convert angle x from radians to degrees and vice versa.
    - `math.log(x, base)`, `math.log10(x)`, `math.log2(x)`: Logarithms.
    - `math.exp(x)`: `e**x`.
    - `math.ceil(x)`, `math.floor(x)`: Ceiling and floor.
    - `math.fabs(x)`: Absolute value.
    - `math.factorial(x)`
    - `math.gcd(a, b)`: Greatest common divisor.
- **Example**:
```python
import math

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 2.3: {math.ceil(2.3)}") # 3
print(f"Floor of 2.7: {math.floor(2.7)}")   # 2
```
- **Where to find examples**: `ShortestPath_Algorithm.py` (uses `float('inf')` which is related, but not directly from `math` module for this specific constant).

### `random` module
- Implements pseudo-random number generators for various distributions. **Not suitable for cryptographic purposes** (use `secrets` module for that).
    - `random.random()`: Random float in `[0.0, 1.0)`.
    - `random.uniform(a, b)`: Random float in `[a, b]` or `[a, b)`.
    - `random.randint(a, b)`: Random integer in `[a, b]` (inclusive).
    - `random.randrange(start, stop[, step])`: Random integer from `range(start, stop, step)`.
    - `random.choice(seq)`: Random element from a non-empty sequence.
    - `random.choices(population, weights=None, cum_weights=None, k=1)`: Return a k-sized list of elements chosen from the population with replacement.
    - `random.sample(population, k)`: Random k-length list of unique elements from population.
    - `random.shuffle(x)`: Shuffle sequence `x` in place.
    - `random.seed(a=None, version=2)`: Initialize the random number generator.
- **Example**:
```python
import random

print(f"Random float: {random.random()}")
print(f"Random integer (1-10): {random.randint(1, 10)}")
my_list_rand = [1, 2, 3, 4, 5]
print(f"Random choice: {random.choice(my_list_rand)}")
random.shuffle(my_list_rand)
print(f"Shuffled list: {my_list_rand}")
```
- **Where to find examples**: `Pasword_Generator.py` uses `secrets.choice`, which is the secure alternative.

### `itertools` module
- Provides functions creating iterators for efficient looping. Many of these are building blocks for more complex iteration patterns.
    - **Infinite Iterators**: `count(start=0, step=1)`, `cycle(iterable)`, `repeat(object[, times])`.
    - **Iterators Terminating on the Shortest Input Sequence**: `accumulate()`, `chain()`, `compress()`, `dropwhile()`, `filterfalse()`, `groupby()`, `islice()`, `starmap()`, `takewhile()`, `tee()`, `zip_longest()`.
    - **Combinatoric Iterators**: `product()`, `permutations()`, `combinations()`, `combinations_with_replacement()`.
- **Example**:
```python
import itertools

# count - infinite counter
# for i in itertools.count(10, 2):
#     if i > 20: break
#     print(i) # 10, 12, 14, 16, 18, 20

# cycle - repeat elements of an iterable
# c = 0
# for item in itertools.cycle("AB"):
#     if c > 5: break
#     print(item) # A, B, A, B, A, B
#     c += 1

# chain - combine multiple iterables
for i in itertools.chain([1, 2], "CD", (3, 4)):
    print(i, end=" ") # 1 2 C D 3 4
print()

# permutations
print(list(itertools.permutations("ABC", 2))) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# combinations
print(list(itertools.combinations([1, 2, 3, 4], 3))) # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
```
- **Where to find examples**: Coming Soon.

## Virtual Environments
- **What they are**: Isolated Python environments that allow you to manage project-specific dependencies separately from your global Python installation and other projects.
- **Why use them**:
    - Avoids conflicts between project dependencies (e.g., Project A needs Lib v1.0, Project B needs Lib v2.0).
    - Keeps your global Python site-packages directory clean.
    - Makes projects self-contained and reproducible.
- **How they work (using `venv` module, built-in since Python 3.3)**:
    1.  **Create**: `python -m venv my_project_env` (creates a directory `my_project_env`)
    2.  **Activate**:
        -   Windows: `my_project_env\Scripts\activate`
        -   macOS/Linux: `source my_project_env/bin/activate`
        (Your shell prompt usually changes to indicate the active environment).
    3.  **Install packages**: `pip install package_name` (installs into the active venv).
    4.  **List installed packages**: `pip list` or `pip freeze > requirements.txt` (to save dependencies).
    5.  **Deactivate**: `deactivate` (from anywhere in the shell).
- **Other tools**: `conda` (especially for scientific computing, manages Python versions and packages), `poetry`, `pipenv`.
- **Example**:
```bash
# In your terminal/command prompt
# python3 -m venv myenv  # Create a virtual environment named 'myenv'
# source myenv/bin/activate  # On macOS/Linux
# # myenv\Scripts\activate  # On Windows

# (myenv) $ pip install requests  # Install 'requests' package into 'myenv'
# (myenv) $ python your_script_using_requests.py
# (myenv) $ pip freeze > requirements.txt # Save dependencies
# (myenv) $ deactivate
```
- **Where to find examples**: This is a workflow, not directly in code files.

## The Walrus Operator (`:=`)
- **What it is**: (Python 3.8+) Assignment Expressions. Allows you to assign a value to a variable as part of a larger expression.
- **How it works**: `(name := expression)`. The value of `expression` is assigned to `name`, and the expression itself also evaluates to this value.
- **Use Cases**: Can simplify some code patterns, especially in `if` statements or `while` loops where you need to use a value immediately after computing it.
- **Example**:
```python
# Without walrus operator
line = input("Enter something (or 'quit'): ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter something (or 'quit'): ")

# With walrus operator
while (line := input("Enter something (or 'quit'): ")) != "quit":
    print(f"You entered: {line}")

# Another example
my_list = [1, 2, 3, 4, 5, 6]
if (n := len(my_list)) > 5:
    print(f"List is too long ({n} elements).")

# Can be useful in comprehensions (though sometimes less readable)
# data = [y for x in some_iterable if (y := process(x)) is not None]
```
- **Where to find examples**: Coming Soon.

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

### Shortest Path Algorithm
This module demonstrates basic shortest path logic. The updated code includes:
- A function called “shortest_path” that computes both paths and distances for each node.
- A Dijkstra-based function for computing shortest distances, using a priority queue (heapq).
- In-depth comments describing every step of the flow, from initializing data structures to printing or returning final results.

This cheat sheet covers the main Python concepts used throughout the repository's projects. Each project demonstrates different aspects of scientific computing and Python programming. It will be updated as more projects are added.
