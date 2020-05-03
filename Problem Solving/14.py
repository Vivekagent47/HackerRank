#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def find_lcm(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm, a[i])
    return lcm

def find_gcd(l):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    n =1
    f = l[0]
    while n != len(l):
        f = gcd(f,l[n])
        if  f == 1:
            return 1
        else:
            n = n + 1          
    return f
    
def getTotalX(a, b):
    # Write your code here
    lcm = find_lcm(a)
    gcd = find_gcd(b)
    count = 0
    j, i = 1, lcm
    while i  <= gcd :
        i = lcm*j
        if gcd%i == 0:
            count += 1
        j += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
