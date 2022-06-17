#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    results = {}   
    for i in range(len(arr)- 1):
        diff = abs(arr[i] - arr[i+1])    
        if diff in results:
            results[diff] += [arr[i], arr[i+1]]
        else:
            results[diff] = [arr[i], arr[i+1]]
    answer = min(results.keys())
    return results[answer]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()