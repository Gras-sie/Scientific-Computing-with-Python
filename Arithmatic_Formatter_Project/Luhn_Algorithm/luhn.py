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