# Enter your code here. Read input from STDIN. Print output to STDOUT

from re import match, compile
patt = compile('^[-+]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(patt.match(input())))