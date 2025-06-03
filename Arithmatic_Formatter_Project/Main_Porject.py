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
