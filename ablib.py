import math
import itertools
import aclib


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
    sorted_array = list(map(lambda x: x[0].lower(), sorted_array))
    return sorted_array


# Aufgabe 14
def computeKeyPairs(char_list):
    output = [element for element in itertools.product(char_list, repeat=2) if element[0] != element[1]]
    return output


# Aufgabe 15
def analyzeCipherText(cipher_text, char_pairs):
    output = []
    for element in char_pairs:
        c_E = ord(element[0]) - 97
        c_N = ord(element[1]) - 97
        a = (3 * (c_N - c_E)) % 26
        b = (c_E - 4 * a) % 26

        if math.gcd(a, 26) != 1:
            continue
        decrypt = aclib.acDecrypt(a, b, cipher_text)
        output.append(decrypt)

    [print(result[:50]) for result in output]

    return output
