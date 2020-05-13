import numpy

m = int(input().split()[0])
matrix = numpy.array([input().split() for _ in range(m)],int)

print(numpy.max(numpy.min(matrix,axis=1)))