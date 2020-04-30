# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
lst = list(map(str, input().split()))
cond1 = all([int(i)>0 for i in lst])
cond2 = any([j == j[::-1] for j in lst])
print(cond1 and cond2)