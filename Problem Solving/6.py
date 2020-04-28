#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    neg_count = len(list(filter(lambda x: (x < 0), arr)))
    pos_count = len(list(filter(lambda x: (x > 0), arr))) 
    zero_count = len(list(filter(lambda x: (x == 0), arr)))  
    print(pos_count/len(arr))
    print(neg_count/len(arr))
    print(zero_count/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)