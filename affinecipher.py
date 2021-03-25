# Aufgabe 8

import argparse
import aclib

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e", "--encrypt", help="Mode for encrypting a file", action="store_true")
group.add_argument("-d", "--decrypt", help="Mode for decrypting a file", action="store_true")
parser.add_argument("-k", "--key", help="Enter the key to decrypt or encrypt. e.g. db (3,1)", required=True)
parser.add_argument("-f", "--file", help="Path to the file you want to encrypt or decrypt", required=True)
args = parser.parse_args()

key = list(args.key)
if len(key) != 2:
    print("Error!\nKey needs to consist of exactly two characters!")
    exit()
a = ord(key[0]) - 97
b = ord(key[1]) - 97

with open(args.file, "r") as handle:
    content = handle.readlines()
content = ''.join(list(map(lambda x: x.strip().replace(" ", ""), content)))

if args.decrypt:
    print(f"Decrypted message: {aclib.acDecrypt(a, b, content)}")

if args.encrypt:
    print(f"Encrypted message: {aclib.acEncrypt(a, b, content)}")
