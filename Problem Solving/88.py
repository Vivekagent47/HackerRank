#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations_with_replacement 


# Complete the stones function below.
def stones(n, a, b):
    mas = []
    res = list(combinations_with_replacement ([a,b],n-1))
    for a in res:
        mas.append(sum(list(a)))
    return sorted(list(set(mas)))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
