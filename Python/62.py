#!/bin/python3

import math
import os
import random
import re
import sys

def get_key(val,d):
    for key, value in d.items(): 
        if val == value: 
            return key 


s = input()
d = dict()
for ele in list(sorted(s)):
    if ele in d.keys():
        d[ele] = d[ele] + 1
    else:
        d[ele] = 1 
d_value = sorted(d.values())[-3:]

for i in range(2,-1,-1):
    key = get_key(d_value[i],d)
    print(key,d_value[i])
    del d[key]