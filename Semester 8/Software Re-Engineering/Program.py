import sys
import re

if len(sys.argv) != 2:
    print("Usage: python symbol_table.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# read the file
with open(filename, "r") as f:
    contents = f.read()

# remove comments and whitespace
contents = re.sub(r"(\".*?\"|\'.*?\')|(#.*)", "", contents, flags=re.DOTALL)
contents = "".join(contents.split())

# create the symbol table
symbol_table = {}
for char in contents:
    if char not in symbol_table:
        symbol_table[char] = 1
    else:
        symbol_table[char] += 1

# print the symbol table and frequencies in a table
print("Symbol\tFrequency")
print("------\t---------")
for symbol, freq in symbol_table.items():
    print(symbol + "\t" + str(freq))
