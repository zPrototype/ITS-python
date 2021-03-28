import re
import math
from itertools import product


# Aufgabe 1
def decode(text):
    output = [ord(x) - 97 for x in re.sub('[^a-zA-Z]+', '', text.lower().strip())]
    return output


# Aufgabe 2
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


# Aufgabe 4
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


# Aufgabe 5
def acDecrypt(a, b, cipher_text):
    output = []
    # Error handling
    if a not in key_table.keys():
        print("Error wrong key")
        print("''")
        return ""

    cipher_text = decode(cipher_text)
    for i in range(len(cipher_text)):
        y = key_table[a] * (cipher_text[i] - b) % 26
        output.append(chr(y + 97))
    return ''.join(output)


# Aufgabe 6
acEncrypt(3, 1, "strenggeheim")  # DGANOTTNWNZL
acDecrypt(15, 8, "IFFYVQMJYFFDQ")  # affinechiffre


# Aufgabe 11
def computeFrequencyTable(char_list):
    frequency_table = dict((x, char_list.count(x)) for x in set(char_list))
    return frequency_table


# Aufgabe 12
def printFrequencyTable(freq_table):
    [print(f"{chr(key + 97)} : {value}") for key, value in freq_table.items()]


# Aufgabe 13
def computeMostFrequentChars(freq_table, n):
    sorted_array = sorted(freq_table.items(), key=lambda x: x[1])
    sorted_array.reverse()
    sorted_array = sorted_array[:n]
    sorted_array = list(map(lambda x: x[0], sorted_array))
    return sorted_array


# Aufgabe 14
def computeKeyPairs(char_list):
    output = [element for element in product(char_list, repeat=2) if element[0] != element[1]]
    return output


# Aufgabe 15
def analyzeCipherText(cipher_text, char_pairs):
    for element in char_pairs:
        c_E = ord(element[0]) - 97
        c_N = ord(element[1]) - 97
        a = (3 * (c_N - c_E)) % 26
        b = (c_E - 4 * a) % 26
        if math.gcd(a, 26) != 1:
            continue
        decrypt = acDecrypt(a, b, cipher_text)
        decrypt = ''.join(decrypt)
        print(decrypt[:50])

# secret = "DGANOTTNWNZL"
# secret = list(secret)
# freq_table = computeFrequencyTable(secret)
# most_freq_chars = computeMostFrequentChars(freq_table, 6)
# computeKeyPairs(most_freq_chars)
# analyzeCipherText("DGANOTTNWNZL", [("n", "o")])
