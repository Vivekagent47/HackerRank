# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

letter , n = map(str, input().split())

for i in range(1, int(n)+1):
    for j in combinations(sorted(letter), i):
        print(''.join(j))