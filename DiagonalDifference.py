#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    count = 0
    a = 0
    b = 0
    for i in range(0,len(arr)):
        for j in range(len(arr[i])):
            if j == count:
                a += arr[i][j]
        count += 1
    count -= 1
    for i in range(len(arr)):
        for j in range(len(arr[i])-1,-1,-1):
            if j == count:
                b += arr[i][j]
        count -= 1
    if a > b:
        return(a-b)
    else:
        return(b-a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()