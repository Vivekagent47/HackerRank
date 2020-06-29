#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, P, N = 1):
    temp = N**P
    if temp > X:
        return 0
    elif temp == X:
        return 1
    return powerSum(X, P, N+1) + powerSum(X-temp, P, N+1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
