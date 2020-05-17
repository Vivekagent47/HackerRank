#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(lst):
    list_y = list()
    p = dict()    
    for item in range(len(lst)):
        p[item+1]=lst[item]

    for x in range(1,(len(lst)+1)):
        for y in lst:
            if p[p[y]] == x:
                list_y.append(y) 
    return list_y


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
