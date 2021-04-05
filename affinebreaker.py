import argparse
import ablib

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", help="Enter the path to the file you want to analyze", required=True)
args = parser.parse_args()

with open(args.file, "r") as handle:
    content = handle.readlines()
content = ''.join(list(map(lambda x: x.strip(), content)))

frequency_table = ablib.computeFrequencyTable(list(content))
n_most_freq_chars = ablib.computeMostFrequentChars(frequency_table, 20)
key_pairs = ablib.computeKeyPairs(n_most_freq_chars)

ablib.analyzeCipherText(content, key_pairs)
