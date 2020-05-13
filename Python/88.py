import numpy

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

print(numpy.inner(arr_A, arr_B))
print(numpy.outer(arr_A, arr_B))

