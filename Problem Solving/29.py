#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reversDigits(n): 
    rev=0
    while n > 0:
        dig = n%10
        rev = rev*10 + dig
        n = n//10
    return rev

def beautifulDays(i, j, k):
    day = 0
    while i <= j:
        if abs(i - reversDigits(i))%k == 0:
            day = day + 1
        i += 1
    return day

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
