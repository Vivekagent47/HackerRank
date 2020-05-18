#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the pairs function below.
def pairs(k, arr):
    count = 0
    num = set()
    for ele in arr:
        if (ele+k) in num:
            count += 1
        if (ele-k) in num:
            count += 1
        num.add(ele)
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
