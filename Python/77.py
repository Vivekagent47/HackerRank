import numpy

n, m = map(int, input().split())
arr = [input().strip().split() for _ in range(n)]
array = numpy.array(arr, int)

print (array.transpose())
print (array.flatten())