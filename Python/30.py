# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string, n = input().split()
num = int(n)
string_sort = ''.join(sorted(string))
# print(string_list)
lst = list(permutations(string_sort,num))
for i in range(len(lst)):
    for j in range(num):
        print(lst[i][j],end="")
    print()
