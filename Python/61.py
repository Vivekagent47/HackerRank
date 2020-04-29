# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
setA = set(input().split())
for _ in range(int(input())):
    command, *args = input().split()
    setB = set(input().split())
    getattr(setA, command)(setB) 

print(sum(map(int, setA)))