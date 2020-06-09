import numpy

n = int(input())
arr = list()

for _ in range(n):
    temp = list(map(float, input().split()))
    arr.append(temp)

print(round(numpy.linalg.det(arr),2))