#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x = sorted(x)
    ans, i = 0, 0
    while i < len(x):
        loc = x[i]
        while (i < len(x)) and (x[i] <= loc+k):
            i = i + 1
        ans = ans + 1
        loc = x[i - 1]
        while  (i < len(x)) and (x[i] <= loc+k):
            i = i + 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
