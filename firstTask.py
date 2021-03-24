import re


def decode(text):
    output = []
    [output.append(ord(x) - 97) for x in re.sub('[^a-zA-Z]+', '', text.lower().strip())]
    print(output)
    return output


def encode(char_list):
    output = []
    [output.append(chr(x + 97)) for x in char_list]
    result = ''.join(output)
    print(result)


decode("Hallo Welt!4324__+*#")
encode(decode("nachricht!!!!"))
