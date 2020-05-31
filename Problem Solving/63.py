#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    e = arr[len(arr)-1]
    ar = arr[0:len(arr)-1]
    l = len(ar)
    last = l-1
    parr = []
    while last > -1:
        tmp = ar[last]
        if tmp < e:
            break
        parr = ar[0:last] + [tmp] + ar[last:l]     
        
        print(" ".join(str(s) for s in parr))
        last = last-1
    parr[last+1] = e
    print(" ".join(str(s) for s in parr))
 

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
