#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallest = max(ar)
    count = 1
    ar.remove(tallest)
    for ele in ar:
        if ele == tallest:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()