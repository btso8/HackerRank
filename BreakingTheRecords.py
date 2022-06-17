#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    minBreak = 0
    maxBreak = 0
    currentMin = max(scores) + 1
    currentMax = min(scores) - 1
    for val in scores:
        if val > currentMax and val < currentMin:
            currentMin = val
            currentMax = val
        elif val > currentMax:
            maxBreak += 1
            currentMax = val
        elif val < currentMin:
            minBreak += 1
            currentMin = val
    return(maxBreak,minBreak)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
