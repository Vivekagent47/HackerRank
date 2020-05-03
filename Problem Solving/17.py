#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(n, ar):
    ids = [0] * 5
    maxN = 0
    id = 1
    for i in range(n):
        ids[ar[i] - 1] += 1
        if(ids[ar[i] - 1] > maxN):
            maxN = ids[ar[i] - 1]
            id = ar[i]
        elif(ids[ar[i] - 1] == maxN and ar[i] < id):
            id = ar[i]
    return id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr_count, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
