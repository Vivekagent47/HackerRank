# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

s = input()

print(*sorted(s, key=(string.ascii_letters + '1357902468').index), sep='')