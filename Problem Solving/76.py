#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_fall = 0
    orange_fall = 0
    home_len = t - s
    apple_dist = s - a
    orange_dist = t - b
    for ele in apples:
        if ele >= apple_dist and ele <= (apple_dist + home_len):
            apple_fall = 1 + apple_fall
    print(apple_fall)
    for ele in oranges:
        if ele <= orange_dist and ele >= (orange_dist - home_len):
            orange_fall = 1 + orange_fall
    print(orange_fall)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
