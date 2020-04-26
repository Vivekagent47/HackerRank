# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
setA = set(map(int, input().split()))
m = int(input())
setB = set(map(int, input().split()))
final = sorted(setA.difference(setB).union(setB.difference(setA)))

for ele in final:
    print(ele)
