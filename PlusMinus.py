#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arrayLength = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for val in arr:
        if val > 0:
            positive += 1
        elif val < 0:
            negative += 1
        else:
            zero += 1
    print(positive/arrayLength)
    print(negative/arrayLength)
    print(zero/arrayLength)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
