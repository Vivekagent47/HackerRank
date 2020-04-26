# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array = list(map(int, input().split()))
listA = set(map(int, input().split()))
listB = set(map(int, input().split()))
happiness = 0
for ele in array:
    if ele in listA:
        happiness += 1
    elif ele in listB:
        happiness -= 1
print(happiness)