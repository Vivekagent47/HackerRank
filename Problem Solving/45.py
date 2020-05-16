#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return arr

def biggerIsGreater(w):
    res = ''.join(sorted(w)) 
    if w == res[::-1]:
        return "no answer"
    else:
        lst = [i for i in w]
        ans = ''.join([str(elem) for elem in next_permutation(lst)]) 
        return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
