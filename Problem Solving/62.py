#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the minimumLoss function below.
def minimumLoss(arr):
    ax = sorted(arr)    
    minm = ax[1]-ax[0]
    
    for i in range(2,len(ax)):
        if ((ax[i]-ax[i-1]) < minm) and (arr.index(ax[i]) < arr.index(ax[i-1])):
            minm = ax[i]-ax[i-1]

    return minm


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    price = list(map(int, input().rstrip().split()))
    result = minimumLoss(price)
    fptr.write(str(result) + '\n')
    fptr.close()