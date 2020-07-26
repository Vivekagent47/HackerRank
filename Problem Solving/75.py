#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(n,arr):
    for l in arr:
        l[0] = int(l[0])  # convert first list item to integer
                
    for i in range(n//2): # replace first half with hyphen
        arr[i][1] = "-"
        
    # sort by number into empty list array
    output = [[] for _ in range(n)]
    for l in arr:
        output[l[0]].append(l[1])
        
    print(' '.join(j for i in output for j in i))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(len(arr),arr)


