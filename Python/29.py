# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
shoes = list(map(int, input().split()))
n = int(input())
profit = 0
cou = Counter(shoes)
for i in range(n):
    temp1, temp2 = map(int,input().split())
    if cou[temp1] != 0:
        profit = profit + temp2
        cou[temp1] = cou[temp1] - 1
print(profit)

#without collections.counter() function
# x = int(input())
# shoes = list(map(int, input().split()))
# n = int(input())
# profit = 0

# for i in range(n):
#     temp1, temp2 = map(int,input().split())
#     if temp1 in shoes:
#         profit = profit + temp2
#         shoes.remove(temp1)


# print(profit)