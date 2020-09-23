#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    no_odds = 0
    no_even = 0
    count = 0
    for ele in B:
        if ele%2 == 0:
            no_even += 1
        else:
            no_odds += 1
    if no_odds%2 != 0: 
        return "NO"
    for i in range(len(B)):
        if B[i]%2 == 0:
            pass
        else:
            B[i] += 1
            B[i+1] += 1
            count += 2
    return count    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
