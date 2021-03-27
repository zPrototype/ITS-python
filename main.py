import re


# Aufgabe 1
def decode(text):
    output = [ord(x) - 97 for x in re.sub('[^a-z]+', '', text.lower().strip())]
    print(f"Characters to integers: {output}")
    return output


# Aufgabe 2
def encode(char_list):
    output = [chr(x + 97) for x in char_list]
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
    output = ''.join(encode(output)).upper()
    print(f"Encrypted message: {output}")


# Aufgabe 5
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
        output.append(y)
    print(encode(output))


# Aufgabe 6
acEncrypt(3, 1, "strenggeheim")  # DGANOTTNWNZL
acDecrypt(15, 8, "IFFYVQMJYFFDQ")  # affinechiffre


# Aufgabe 11
def computeFrequencyTable(char_list):
    frequency_table = dict((x, char_list.count(x)) for x in set(char_list))
    return frequency_table


computeFrequencyTable([4, 8, 13, 11, 0, 13, 6, 4, 17, 19, 4, 23, 19, 14, 7, 13, 4, 18, 8, 13, 13])


# Aufgabe 12
def printFrequencyTable(freq_table):
    [print(f"{chr(key + 97)} : {value}") for key, value in freq_table.items()]


printFrequencyTable(computeFrequencyTable([4, 8, 13, 11, 0, 13, 6, 4, 17, 19, 4, 23, 19, 14, 7, 13, 4, 18, 8, 13, 13]))


# Aufgabe 13
def computeMostFrequentChars(freq_table, n):
    sorted_array = sorted(freq_table.items(), key=lambda x: x[1])
    sorted_array.reverse()
    sorted_array = sorted_array[:n]
    sorted_array = list(map(lambda x: x[0], sorted_array))
    print(sorted_array)
    return sorted_array


computeMostFrequentChars(
    computeFrequencyTable([4, 8, 13, 11, 0, 13, 6, 4, 17, 19, 4, 23, 19, 14, 7, 13, 4, 18, 8, 13, 13]), 6)
