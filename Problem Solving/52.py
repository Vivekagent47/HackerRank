#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 1
    special_page = 0
    for i in arr:
        for j in range(1,i+1):
            if j == page:
                special_page += 1
            if j%k == 0:
                page += 1
        if i%k !=0:
            page += 1
    return special_page

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    print(result)
