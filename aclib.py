# Aufgabe 7

import re


def decode(text):
    output = [ord(x) - 97 for x in re.sub('[^a-zA-Z]+', '', text.lower().strip())]
    return output


def encode(char_list):
    output = [chr(x + 97) for x in char_list]
    output = ''.join(output)
    return output


# Aufgabe 3
key_table = {
    1: 1,
    3: 9,
    5: 21,
    7: 15,
    9: 3,
    11: 19,
    15: 7,
    17: 23,
    19: 11,
    21: 5,
    23: 17,
    25: 25
}


def acEncrypt(a, b, plain_text):
    output = []

    # Error handling
    if a not in key_table.keys():
        print("Error wrong key")
        print("''")
        exit()

    # Encryption
    plain_text = decode(plain_text)
    for i in range(len(plain_text)):
        y = (a * plain_text[i] + b) % 26
        output.append(y)
        i += 1
    return ''.join(encode(output)).upper()


def acDecrypt(a, b, cipher_text):
    output = []
    # Error handling
    if a not in key_table.keys():
        print("Error wrong key")
        print("''")
        exit()

    cipher_text = decode(cipher_text)
    for i in range(len(cipher_text)):
        y = key_table[a] * (cipher_text[i] - b) % 26
        output.append(chr(y + 97))
    return ''.join(output)
