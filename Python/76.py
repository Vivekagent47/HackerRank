import numpy

arr = input().strip().split()
my_array = numpy.array(arr,int)

print(numpy.reshape(my_array,(3,3)))
