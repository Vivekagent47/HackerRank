# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

string, n = input().split()
num = int(n)
string_sort = ''.join(sorted(string))
# print(string_list)
lst = list(combinations_with_replacement(string_sort,num))
for i in range(len(lst)):
    for j in range(num):
        print(lst[i][j],end="")
    print()