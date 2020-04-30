# Enter your code here. Read input from STDIN. Print output to STDOUT

setA = set(map(int, input().split()))
n = int(input())
count = 0
for i in range(1,n+1):
    temp = set(map(int, input().split()))
    if setA.issuperset(temp):
        count += 1
    else:
        pass

if count == n:
    print("True")
else:
    print("False")