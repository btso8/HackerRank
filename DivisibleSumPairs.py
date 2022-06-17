#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def pairArray(ar, finishedArray):
    if len(ar) == 1:
        return(finishedArray)
    else:
        for val in ar[1:]:
            finishedArray += [[ar[0],val]]
        return(pairArray(ar[1:],finishedArray))

def divisibleSumPairs(n, k, ar):
    numOfDivPair = 0
    ar.sort()
    pairAr = pairArray(ar, [])
    for pair in pairAr:
        if sum(pair) % k == 0:
            numOfDivPair += 1
    return(numOfDivPair)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()