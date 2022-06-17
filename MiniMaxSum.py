#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maxArr = arr.copy()
    minArr = arr.copy()
    maxArr.remove(min(maxArr))
    minArr.remove(max(minArr))
    print(sum(minArr), sum(maxArr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
