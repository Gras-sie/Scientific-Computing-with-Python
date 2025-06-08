"""
PYTHON CONCEPTS CHEAT SHEET:

MODULES:
- Modules are Python files containing code that can be reused
- Import syntax: import module_name or from module_name import specific_item
- Common modules used here:
    * re: Regular expressions for pattern matching
    * secrets: Secure random number generation
    * string: String constants and operations

VARIABLES:
- Variables are containers for storing data values
- No need to declare type (dynamic typing)
- Example: my_var = value

STRINGS:
- Sequence of characters
- Created with single or double quotes: 'hello' or "hello"
- String concatenation uses + operator
- f-strings allow embedding expressions: f"value is {variable}"

TUPLES:
- Immutable (unchangeable) ordered sequences of values.
- Created using parentheses: (value1, value2, ...).
- Used to group related items together, especially when the order matters and the collection should not be modified.
- A 2-element tuple can represent a pair of related data (e.g., a coordinate (x, y), or a setting and its value).
- Access elements by index: tuple[0].
- Example in code: (nums, r'\d') is a 2-element tuple representing a constraint (minimum count) and its corresponding regex pattern.

LISTS:
- Mutable sequences of values
- Created using square brackets: [value1, value2]
- Can contain mixed types
- Example in code: constraints = [(nums, r'\d'), ...]

FUNCTIONS:
- Blocks of reusable code
- Defined using 'def' keyword
- Can have default parameters
- Example: def function_name(parameter=default_value):

LOOPS:
- while loop: Repeats while condition is True
- for loop: Iterates over a sequence
- Example: for item in sequence:

CONDITIONALS:
- if statement: Execute code if condition is True
- Example: if condition:

REGEX (Regular Expressions):
- Pattern matching in strings
- r'\d' matches any digit
- r'[A-Z]' matches any uppercase letter
- Pattern examples:
    * \d - any digit
    * [A-Z] - any uppercase letter
    * [a-z] - any lowercase letter
    * [symbols] - any special character

BUILT-IN FUNCTIONS:
- len(): Returns length of sequence
- all(): Returns True if all elements are True
- range(): Creates a sequence of numbers

GENERATOR EXPRESSIONS:
- Creates iterator on-the-fly
- Syntax: (expression for item in sequence)
- More memory efficient than list comprehension
"""

# Import required modules
import re              # Regular expressions module for pattern matching
import secrets        # Module for generating cryptographically strong random numbers
import string         # Module containing string constants

# Password generation function with default parameters
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a random password with specified constraints
    Parameters:
    - length: Total length of password (default: 16)
    - nums: Minimum number of numerals required (default: 1)
    - special_chars: Minimum number of special characters required (default: 1)
    - uppercase: Minimum number of uppercase letters required (default: 1)
    - lowercase: Minimum number of lowercase letters required (default: 1)
    """
    # String constants for different character types
    letters = string.ascii_letters    # Contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits           # Contains '0123456789'
    symbols = string.punctuation     # Contains '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    # Combine all possible characters into one string
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate random password of specified length
        for _ in range(length):
            password += secrets.choice(all_characters)  # Randomly select one character at a time
        
        # List of tuples. Each tuple groups a minimum count with its corresponding regex pattern.
        constraints = [
            (nums, r'\d'),                    # Tuple: (minimum_digits, digit_pattern)
            (special_chars, fr'[{symbols}]'),  # Tuple: (minimum_special_chars, special_char_pattern)
            (uppercase, r'[A-Z]'),            # Tuple: (minimum_uppercase, uppercase_pattern)
            (lowercase, r'[a-z]')             # Tuple: (minimum_lowercase, lowercase_pattern)
        ]

        # Check if all constraints are met
        # all() returns True if all elements in the iterator are True
        # re.findall() returns a list of all non-overlapping matches in the password
        if all(
            constraint <= len(re.findall(pattern, password))  # Check if minimum count <= actual count
            for constraint, pattern in constraints            # Iterate through each constraint tuple
        ):
            break  # Exit loop if all constraints are met
    
    return password  # Return the generated password that meets all requirements

# Generate a new password using default parameters    
new_password = generate_password()
print('Generated password:', new_password)