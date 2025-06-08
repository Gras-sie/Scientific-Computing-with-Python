"""
PYTHON ARITHMETIC FORMATTER CONCEPTS CHEAT SHEET:

FUNCTION DEFINITIONS:
- Define function with: def function_name(parameters):
- Default parameters: def function(param=default_value):
- Return values: return expression

STRING FORMATTING:
- f-strings: f"Value: {variable}" interpolates variables into strings
- String methods:
  * rjust(width): Right-justify text in field of width
  * ljust(width): Left-justify text in field of width
  * join(iterable): Join elements of iterable with string as separator

LISTS:
- Create list: my_list = [value1, value2, ...]
- Append to list: my_list.append(value)
- List operations: len(list), sum(list), max(list), min(list)
- List comprehension: [expression for item in iterable if condition]

CONTROL FLOW:
- Conditionals: if condition: ... elif condition: ... else: ...
- Boolean operators: and, or, not
- Comparison operators: ==, !=, <, >, <=, >=

ERROR HANDLING:
- Early returns with error messages
- Input validation before processing
- Consistent error message formats

STRING OPERATIONS:
- Concatenation: string1 + string2
- Repetition: '-' * 5 creates '-----'
- Splitting: 'a b c'.split() creates ['a', 'b', 'c']

TYPE CONVERSION:
- str(value): Convert to string
- int(string): Convert string to integer
- float(string): Convert string to float

TEXT ALIGNMENT:
- Right alignment: string.rjust(width)
- Left alignment: string.ljust(width)
- Center alignment: string.center(width)

MULTI-LINE STRING FORMATTING:
- Using newline character '\n' to create multi-line output
- Building formatted output line by line
"""

def arithmetic_arranger(problems, show_answers=False):
    # Error check 1: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = []
    bottom_row = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first, operator, second = parts

        # Error check 2: Invalid operator
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        # Error check 3: Non-digit characters
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        # Error check 4: Operand too long
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width
        width = max(len(first), len(second)) + 2  # 2 extra for operator and space

        # Format each line
        top_row.append(first.rjust(width))
        bottom_row.append(operator + ' ' + second.rjust(width - 2))
        dashes.append('-' * width)

        # If showing answers, calculate and format result
        if show_answers:
            if operator == '+':
                result = str(int(first) + int(second))
            else:
                result = str(int(first) - int(second))
            results.append(result.rjust(width))

    # Join each row with 4 spaces between problems
    arranged_top = '    '.join(top_row)
    arranged_bottom = '    '.join(bottom_row)
    arranged_dashes = '    '.join(dashes)
    
    if show_answers:
        arranged_results = '    '.join(results)
        return f"{arranged_top}\n{arranged_bottom}\n{arranged_dashes}\n{arranged_results}"
    else:
        return f"{arranged_top}\n{arranged_bottom}\n{arranged_dashes}"
