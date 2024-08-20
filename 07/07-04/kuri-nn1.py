fname = 'out_test.txt'
s = 'Hello out_test.txt'
with open(fname, 'w') as f:
    f.write(s)

with open(fname, 'r') as f:
    for line in f:
        print(line, end="")
