#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    if re.search(r'\d',password):
        count+=1
    if re.search(r'[a-z]',password):
        count+=1
    if re.search(r'[A-Z]',password):
        count+=1
    if re.search(r'[!@#\$%\^&\*\(\)\-\+]',password):
        count+=1
    return max(6-n,4-count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
