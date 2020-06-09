import numpy

arr  = numpy.array(list(map(float, input().split())))

numpy.set_printoptions(legacy='1.13')

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))