#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = scores[0]
    low = scores[0]
    high_count, low_count = 0, 0
    for i in range(len(scores)):
        if scores[i] < low:
            low = scores[i]
            low_count += 1
        elif scores[i] > high:
            high = scores[i]
            high_count += 1 
    return [high_count, low_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
