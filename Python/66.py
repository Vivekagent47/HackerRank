# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
lst = list(map(int, input().split()))

room_set = set(lst)

for ele in room_set:
    lst.remove(ele)

print(room_set.difference(set(lst)).pop())