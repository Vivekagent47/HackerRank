import numpy

n,m = map(int, input().split())

arr = list()
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

my_arr = numpy.array(arr)

numpy.set_printoptions(legacy='1.13')

print(numpy.mean(my_arr, axis = 1))
print(numpy.var(my_arr, axis = 0))
print(numpy.std(my_arr, axis = None))
