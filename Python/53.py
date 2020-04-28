
from collections import deque

d = deque()

for _ in range(int(input())):
    temp = input().split()
    getattr(d, temp[0])(*[temp[1]] if len(temp) > 1 else [])

print(*[ele for ele in d])
