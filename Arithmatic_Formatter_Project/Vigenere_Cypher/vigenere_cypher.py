"""
PYTHON CRYPTOGRAPHY CONCEPTS CHEAT SHEET:

STRINGS AND CHARACTERS:
- Strings are sequences of characters, accessed by index: string[index]
- String methods: lower(), upper(), isalpha(), find(), index()
- String slicing: string[start:end:step]

STRING MANIPULATION:
- Concatenation with +: 'hello' + 'world' -> 'helloworld'
- Join method: ''.join(list_of_strings) combines list elements
- Character checking: char.isalpha(), char.isupper(), char.islower()

MODULAR ARITHMETIC:
- Remainder operator: a % b gives remainder of a divided by b
- Wrapping around: (index + shift) % 26 ensures value stays in range 0-25
- Used for cyclic operations like letter shifting in ciphers

CRYPTOGRAPHY BASICS:
- Plaintext: Original readable message
- Ciphertext: Encrypted, unreadable form of the message
- Key: Secret value needed for encryption/decryption
- Encryption: Process of converting plaintext to ciphertext
- Decryption: Process of recovering plaintext from ciphertext

VIGENERE CIPHER:
- Polyalphabetic substitution cipher (uses multiple alphabets)
- Each letter is shifted based on corresponding letter in the key
- Key is repeated to match the length of the message
- Formula for encryption: (plaintext_index + key_index) % 26
- Formula for decryption: (ciphertext_index - key_index) % 26

ITERATION TECHNIQUES:
- Looping through characters: for char in string
- Tracking position: enumerate(string) gives (index, value) pairs
- Key cycling: key_char = key[index % len(key)]

CONTROL FLOW:
- Conditional processing: if condition: ... else: ...
- Preserving non-alphabet chars: if not char.isalpha()
"""

# Example encrypted text and encryption key
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'


# Main Vigenere cipher function that handles both encryption and decryption
# direction=1 for encryption, direction=-1 for decryption
def vigenere(message, key, direction=1):
    key_index = 0  # Track position in the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Reference alphabet for shifting
    final_message = ''

    # Process each character in the input message
    for char in message.lower():
        # Preserve non-alphabetic characters (spaces, punctuation)
        if not char.isalpha():
            final_message += char
        else:        
            # Get the current key character using modular arithmetic
            # This allows the key to repeat if it's shorter than the message
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calculate the shift amount and new letter position
            # For encryption: shift forward by offset
            # For decryption: shift backward by offset
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message


# Wrapper function for encryption (positive direction)
def encrypt(message, key):
    return vigenere(message, key)
    

# Wrapper function for decryption (negative direction)
def decrypt(message, key):
    return vigenere(message, key, -1)


# Example usage of the cipher
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')