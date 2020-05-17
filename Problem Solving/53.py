#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n,like,share):
    if n == 0:
        return like
    else:
        like = like + share//2
        return viralAdvertising(n-1,like, share//2 * 3)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n,0,5)

    fptr.write(str(result) + '\n')

    fptr.close()
