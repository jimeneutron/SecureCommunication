""" Polyalphabetic cipher + 6-bit encoding + digit obfuscation """

import string
import random

# =====================
# CONSTANTS
# =====================
ALPHABET = string.ascii_lowercase
SAFE_CHARS = string.digits + string.punctuation + string.whitespace

# =====================
# POLYALPHABETIC CIPHER
# =====================
def cycle_get(lst, index):
    return lst[index % len(lst)]

def cycle_increment_index(index, lst):
    return (index + 1) % len(lst)

def shift(letter, value):
    return cycle_get(ALPHABET, ALPHABET.index(letter) + value)

def convert_key_to_numbers(key):
    return [ALPHABET.index(i) for i in key]

def encrypt_poly(text, key):
    text = text.lower()
    key_nums = convert_key_to_numbers(key)
    ki = 0
    result = ""

    for char in text:
        if char not in ALPHABET:
            result += char
        else:
            result += shift(char, key_nums[ki])
            ki = cycle_increment_index(ki, key_nums)

    return result

# =====================
# 6-BIT CHARACTER MAP
# =====================
CHAR_TO_BITS = {
    'a':'100000','b':'010000','c':'110000',
    'd':'001000','e':'101000','f':'011000',
    'g':'111000','h':'000100','i':'100100',
    'j':'010100','k':'110100','l':'001100',
    'm':'101100','n':'011100','o':'111100',
    'p':'000010','q':'100010','r':'010010',
    's':'110010','t':'001010','u':'101010',
    'v':'011010','w':'111010','x':'000110',
    'y':'100110','z':'010110',
    ' ':'000000',
    '0':'001001','1':'110110','2':'001110',
    '3':'101110','4':'011110','5':'111110',
    '6':'000001','7':'100001','8':'010001',
    '9':'110001',
    '.':'101001',',':'011001','?':'111001',
    ':':'000101','-':'010101','!':'110101',
    '(':'001101'
}

# =====================
# TEXT → BITSTRING
# =====================
def text_to_bits(text):
    bits = ""
    for char in text:
        if char in CHAR_TO_BITS:
            bits += CHAR_TO_BITS[char]
        else:
            raise ValueError(f"Unsupported character: {char}")
    return bits

# =====================
# BIT OBFUSCATION
# =====================
def obfuscate_bits(bitstring):
    output = []
    for bit in bitstring:
        if bit == '1':
            output.append(str(random.randint(6, 9)))
        else:
            output.append(str(random.randint(0, 4)))
    return "".join(output)

# =====================
# RUN ENCRYPTION
# =====================
plaintext = input("Text to encrypt: ")
secret = input("Secret key: ")

poly_encrypted = encrypt_poly(plaintext, secret)
bitstring = text_to_bits(poly_encrypted)
final_ciphertext = obfuscate_bits(bitstring)

print("\nEncrypted output:")
print(final_ciphertext)
