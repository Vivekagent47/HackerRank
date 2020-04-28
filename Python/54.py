# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
d = dict()

for _ in range(n):
    temp = input()
    if temp in d:
        d[temp] += 1
    else:
        d[temp] = 1

print(len(d))
for value in d.values():
    print(value,end=" ")