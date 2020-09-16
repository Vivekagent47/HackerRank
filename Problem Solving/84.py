#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def removeRepeats(s):
    lst = list(s)
    i = 0 
    while i < len(lst)-1:
        if lst[i]==lst[i+1]:
            del lst[i]
            del lst[i]
            i = 0
            if len(lst) == 0:
                return 'Empty String'
        else:
            i+=1
    return ''.join(lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = removeRepeats(s)

    fptr.write(result + '\n')

    fptr.close()
