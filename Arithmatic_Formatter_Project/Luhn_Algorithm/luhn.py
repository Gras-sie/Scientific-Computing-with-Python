"""
PYTHON LUHN ALGORITHM CONCEPTS CHEAT SHEET:

STRING OPERATIONS:
- String reversal: string[::-1] reverses the string
- String slicing: string[start:stop:step]
  * string[::2] gets every second character (even indices)
  * string[1::2] gets every second character starting from index 1 (odd indices)
- String translation: string.translate(translation_table) replaces characters

DATA VALIDATION:
- Checksum algorithms verify data integrity
- Luhn algorithm: Used to validate credit card numbers, ISBNs, etc.
- Modular arithmetic: num % 10 == 0 checks if number is divisible by 10

INTEGER OPERATIONS:
- Division: number // 10 (floor division, gives integer result)
- Modulo: number % 10 (remainder after division)
- Digit extraction: 
  * last_digit = number % 10
  * first_digit = int(str(number)[0])

STRING MANIPULATION FUNCTIONS:
- str.maketrans(): Create translation table for character replacement
- string.translate(): Apply translation table to string
- string.strip(): Remove characters from beginning and end

LUHN ALGORITHM STEPS:
1. Double every second digit from right to left
2. If doubling results in a two-digit number, add digits together
3. Sum all resulting digits
4. If sum is divisible by 10, number is valid

ITERATION TECHNIQUES:
- For loops: for item in sequence
- String iteration: for char in string
- Reversal iteration: for char in string[::-1]

TYPE CONVERSION:
- str() converts to string
- int() converts to integer
- Character to digit: int(char)
"""

# Function to verify card numbers using the Luhn Algorithm
# This algorithm helps detect accidental errors in card numbers
def verify_card_number(card_number):
    # Step 1: Calculate sum of odd-positioned digits (from right)
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]  # Reverse the card number to simplify processing from right to left
    odd_digits = card_number_reversed[::2]    # Get every other digit

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Step 2: Calculate sum of even-positioned digits (from right)
    # For even positions: multiply by 2 and sum digits if result >= 10
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        # If multiplication results in two digits, add them together
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Step 3: Total both sums and check if divisible by 10
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0

def main():
    # Example card number with hyphens
    card_number = '4111-1111-4555-1142'
    # Remove hyphens and spaces from card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Verify and display result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()