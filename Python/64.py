# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    int(input())
    setA = set(map(int, input().split()))
    int(input())
    setB = set(map(int, input().split()))
    print(setA.issubset(setB))