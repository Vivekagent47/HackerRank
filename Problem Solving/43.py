#!/bin/python3

import math
import os
import random
import re
import sys

# Using index function
def introTutorial2(V, arr):
    if V in arr:
        return arr.index(V)


# Complete the introTutorial function below.
def introTutorial1(V, arr):
    for i in range(len(arr)):
        if arr[i] == V:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial2(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
