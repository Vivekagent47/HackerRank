#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = list(str(input().strip()))
    grid.append(grid_t)

for i in range(1,(n-2)+1):
    for j in range(1,(n-2)+1):
        if grid[i][j]>max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
            grid[i][j]='X'
    
for i in range(n):
    print (''.join(grid[i]))  
