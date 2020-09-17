#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum= 0
    for i in range(0,4):
        for j in range(0,4):
            temp_sum = 0
            temp_sum += arr[i][j]
            temp_sum += arr[i][j+1]
            temp_sum += arr[i][j+2]
            temp_sum += arr[i+1][j+1]
            temp_sum += arr[i+2][j]
            temp_sum += arr[i+2][j+1]
            temp_sum += arr[i+2][j+2]
            
            if (temp_sum > max_sum) or i==0 and j==0:
                max_sum = temp_sum

    print(max_sum)
