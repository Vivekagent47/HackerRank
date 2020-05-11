#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    flag=0
    while(k):
        if len(s) == 0:
            k = k - len(t)
            if k >= 0:
                flag = 1
                break
            break
        elif s in t:
            if s[0] == t[0]:
                if len(t) - len(s) == k:
                    flag = 1
                    break
                elif len(t) - len(s) < k:
                    if len(s)%2 == len(t)%2:
                        if k%2 == 0:
                            flag = 1
                    else:
                        if k%2!=0:
                            flag = 1
                else:
                    break
        s = s[:-1]
        k -= 1
    if flag == 0:
        return 'No'
    return 'Yes'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
