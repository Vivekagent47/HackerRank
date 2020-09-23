#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinussimple(arr):
    pos, neg, zero = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1

    print(pos/len(arr))
    print(neg/len(arr))
    print(zero/len(arr))



# Complete the plusMinus function below.
def plusMinusbetter(arr):
    neg_count = len(list(filter(lambda x: (x < 0), arr)))
    pos_count = len(list(filter(lambda x: (x > 0), arr))) 
    zero_count = len(list(filter(lambda x: (x == 0), arr)))  
    print(pos_count/len(arr))
    print(neg_count/len(arr))
    print(zero_count/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinusbetter(arr)