""" Decryption for polyalphabetic + 6-bit + digit obfuscation """

import string

# =====================
# CONSTANTS
# =====================
ALPHABET = string.ascii_lowercase

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

def decrypt_poly(text, key):
    key_nums = convert_key_to_numbers(key)
    ki = 0
    result = ""

    for char in text:
        if char not in ALPHABET:
            result += char
        else:
            result += shift(char, -key_nums[ki])
            ki = cycle_increment_index(ki, key_nums)

    return result

# =====================
# 6-BIT MAP (REVERSED)
# =====================
BITS_TO_CHAR = {
    '100000':'a','010000':'b','110000':'c',
    '001000':'d','101000':'e','011000':'f',
    '111000':'g','000100':'h','100100':'i',
    '010100':'j','110100':'k','001100':'l',
    '101100':'m','011100':'n','111100':'o',
    '000010':'p','100010':'q','010010':'r',
    '110010':'s','001010':'t','101010':'u',
    '011010':'v','111010':'w','000110':'x',
    '100110':'y','010110':'z',
    '000000':' ',
    '001001':'0','110110':'1','001110':'2',
    '101110':'3','011110':'4','111110':'5',
    '000001':'6','100001':'7','010001':'8',
    '110001':'9',
    '101001':'.','011001':',','111001':'?',
    '000101':':','010101':'-','110101':'!',
    '001101':'('
}

# =====================
# DIGITS → BITS
# =====================
def digits_to_bits(ciphertext):
    bits = ""
    for char in ciphertext:
        if not char.isdigit():
            raise ValueError("Ciphertext must contain digits only")
        bits += '0' if int(char) < 5 else '1'
    return bits

# =====================
# BITS → TEXT
# =====================
def bits_to_text(bits):
    if len(bits) % 6 != 0:
        raise ValueError("Bit length not divisible by 6")

    text = ""
    for i in range(0, len(bits), 6):
        chunk = bits[i:i+6]
        if chunk not in BITS_TO_CHAR:
            raise ValueError(f"Invalid bit chunk: {chunk}")
        text += BITS_TO_CHAR[chunk]

    return text

# =====================
# RUN DECRYPTION
# =====================
ciphertext = input("Encrypted digits: ")
secret = input("Secret key: ")

bitstring = digits_to_bits(ciphertext)
decoded_text = bits_to_text(bitstring)
final_plaintext = decrypt_poly(decoded_text, secret)

print("\nDecrypted output:")
print(final_plaintext)
