import numpy

N = int(input())
arr_a = numpy.array([input().split() for _ in range(N)],int)
arr_b = numpy.array([input().split() for _ in range(N)],int)

print(numpy.dot(arr_a, arr_b))