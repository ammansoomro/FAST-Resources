import sys
import tokenize

if len(sys.argv) != 2:
    print("Usage: python symbol_table.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# read the file
with open(filename, "r") as f:
    contents = f.read()

# tokenize the input
tokens = []
for token in tokenize.generate_tokens(iter(contents.splitlines(keepends=True)).__next__):
    token_type = tokenize.tok_name[token.type]
    token_str = token.string.strip()
    if token_str:
        tokens.append((token_str, token_type))

# create the symbol table
symbol_table = {}
for token in tokens:
    symbol = token[0]
    if symbol not in symbol_table:
        symbol_table[symbol] = 1
    else:
        symbol_table[symbol] += 1

# print the symbol table and frequencies in a table
print("Symbol\tFrequency")
print("------\t---------")
for symbol, freq in symbol_table.items():
    print(symbol + "\t" + str(freq))
