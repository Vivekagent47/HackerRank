#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    arraypair = []

    minimumDiff = 20000001

    for i in range(n-1):
        difference = abs(arr[i] - arr[i+1])
        if difference < minimumDiff:
            arraypair = [arr[i], arr[i+1]]
            minimumDiff = difference
        elif difference == minimumDiff:
            arraypair.append(arr[i])
            arraypair.append(arr[i+1])
    return(arraypair)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
