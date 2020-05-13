import numpy

poly = list(map(float, input().split()))
k = float(input())
print(numpy.polyval(poly, k))
