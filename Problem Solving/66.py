#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    count = 0
    if arr == sorted(arr):
        return 0
    else:
        for i in range(1,len(arr)):
            key = arr[i]
            for j in range(i):
                if j >= 0 and arr[j] > key:
                    arr[i], arr[j] = arr[j], arr[i]
                    count += 1
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
