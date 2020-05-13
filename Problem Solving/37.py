#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    len_array = list()
    minvalue = 0
    while True:
        arr = [i - minvalue for i in arr]
        # print(arr)
        try:
            while True:
                arr.remove(0)
        except ValueError:
            pass
        if arr == []:
            break
        else:
            minvalue = min(arr)
        len_array.append(len(arr))
    return len_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
