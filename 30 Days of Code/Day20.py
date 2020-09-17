#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
t_swap = 0

for i in range(n):
    n_swaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            n_swaps = n_swaps + 1
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            t_swap += 1
    if n_swaps == 0:
        break

print("Array is sorted in", t_swap, "swaps.")
print("First Element:",a[0] )
print("Last Element:",a[-1])
