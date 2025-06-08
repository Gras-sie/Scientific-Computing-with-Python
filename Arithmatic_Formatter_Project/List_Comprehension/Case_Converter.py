"""
PYTHON LIST COMPREHENSION & CASE CONVERSION CHEAT SHEET:

LIST COMPREHENSION:
- Basic syntax: [expression for item in iterable]
- With condition: [expression for item in iterable if condition]
- With if-else: [expression_if if condition else expression_else for item in iterable]
- Nested: [expression for outer_item in outer_iterable for inner_item in inner_iterable]

CASE CONVENTIONS:
- snake_case: words_separated_by_underscores (Python variables, functions)
- camelCase: firstWordLowerCaseRestCapitalized (JavaScript variables)
- PascalCase: AllWordsCapitalized (Python classes)
- kebab-case: words-separated-by-hyphens (HTML attributes, CSS properties)

STRING METHODS FOR CASE:
- upper(): Convert string to uppercase
- lower(): Convert string to lowercase
- capitalize(): Capitalize first letter, rest lowercase
- title(): Capitalize first letter of each word
- swapcase(): Swap case of each character
- isupper(), islower(): Check if string is all upper/lowercase

CHARACTER OPERATIONS:
- isalpha(): Check if character is a letter
- isdigit(): Check if character is a digit
- isalnum(): Check if character is alphanumeric
- isspace(): Check if character is whitespace

STRING JOINING:
- ''.join(list_of_strings): Combine list items into single string
- separator.join(list_of_strings): Join with separator between items

FUNCTIONAL CASE CONVERSION:
- Converting between case conventions requires:
  * Identifying word boundaries (capitals or underscores)
  * Transforming the case appropriately
  * Joining with appropriate separators

ADVANCED STRING MANIPULATION:
- String slicing: string[start:end:step]
- String methods: strip(), lstrip(), rstrip() to remove whitespace
- Regular expressions: For complex pattern matching/replacement
"""

#def convert_to_snake_case(pascal_or_camel_cased_string):
#   snake_cased_char_list = []
#    for char in pascal_or_camel_cased_string:
#        if char.isupper():
#            converted_character = '_' + char.lower()
#            snake_cased_char_list.append(converted_character)
#        else:
#            snake_cased_char_list.append(char)
#    snake_cased_string = ''.join(snake_cased_char_list)
#    clean_snake_cased_string = snake_cased_string.strip('_')

#    return clean_snake_cased_string

def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('i_am_a_pascal_cased_string'))