import re


# Aufgabe 1
def decode(text):
    output = []
    [output.append(ord(x) - 97) for x in re.sub('[^a-zA-Z]+', '', text.lower().strip())]
    print(f"Characters to integers: {output}")
    return output


# Aufgabe 2
def encode(char_list):
    output = []
    [output.append(chr(x + 97)) for x in char_list]
    output = ''.join(output)
    print(f"Integer list to string: {output}")
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


# Aufgabe 4
def acEncrypt(a, b, plain_text):
    output = []

    # Error handling
    if a not in key_table.keys() or b not in key_table.values():
        print("Error wrong key")
        print("''")
        exit()

    # Encryption
    plain_text = decode(plain_text)
    for i in range(len(plain_text)):
        y = (a * plain_text[i] + b) % 26
        output.append(y)
        i += 1
    output = ''.join(encode(output)).upper()
    print(f"Encrypted message: {output}")


acEncrypt(11, 23, "nachricht")
