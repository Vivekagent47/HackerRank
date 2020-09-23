#!/bin/python3

import math
import os
import random
import re
import sys

# Without using python funcrions
def birthdayCakeCandles1(candles):
    count = 1
    tallest = candles[0]
    for i in range(1,len(candles)):
        if tallest == candles[i]:
            count += 1
        if tallest < candles[i]:
            count = 1
            tallest = candles[i]
    return count


# Using some inbuilt python functions
def birthdayCakeCandles2(ar):
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
    result = birthdayCakeCandles2(ar)
    fptr.write(str(result) + '\n')
    fptr.close()