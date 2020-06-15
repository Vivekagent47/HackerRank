#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def partition(arr,low,high): 
    i = ( low-1 )  
    pivot = arr[high]    
  
    for j in range(low , high):
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high):
    if low < high: 
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    quickSort(arr, 0, n-1)

    fptr.write(' '.join(map(str, arr)))
    fptr.write('\n')

    fptr.close()
