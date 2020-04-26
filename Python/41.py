import numpy

n,m = map(int,input().split())
my_array = numpy.array([input().split() for _ in range(n)],int)

print(numpy.prod(numpy.sum(my_array, axis=0),axis=0))