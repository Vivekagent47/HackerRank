#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    d=[]
    for x in a:
        diff = (len(a) -1 - a[::-1].index(x)) - a.index(x)
        if diff > 0:
            d.append(diff)
    if len(d) == 0:
        return -1
    else:
        return min(d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
