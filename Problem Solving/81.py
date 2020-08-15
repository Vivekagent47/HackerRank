#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def minSwaps(arr):
    n = len(arr) 
    arrpos = [*enumerate(arr)] 
    arrpos.sort(key = lambda it:it[1]) 
    vis = {k:False for k in range(n)} 
 
    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue 
        cycle_size = 0
        j = i 
        while not vis[j]:  
            vis[j] = True 
            j = arrpos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans 


def lilysHomework(arr):
    return min(minSwaps(arr), minSwaps(list(reversed(arr))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
