#!/bin/python3

import math
import os
import random
import re
import sys

n,m = map(int, input().split()) 
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
        
arr.sort(key=lambda x : x[k])

for ele in arr:
    print(*ele,sep=" ")



# This is also the solution of the problem but there is an mistake in it thats why all the test cases are not passed
# If any of you found it please correct it

# for i in range(0,n):
#     min_val = arr[i][k]
#     min_index = i
#     for j in range(i,n):
#         if arr[j][k] <= min_val:
#             min_val = arr[j][k]
#             min_index = j
#     for x in range(0,m):
#         arr[i][x], arr[min_index][x] = arr[min_index][x], arr[i][x]

# for i in range(0,n):
#     print(' '.join([str(j) for j in arr[i]]))

