#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    answer = 0
    x = False
    count = 0
    for i in path:
        if count == 0 and i == "U" and x == True:
            count += 1
            x = False
        elif count == 0 and i == "D":
            count -= 1
            answer += 1
            x = True
        elif i == "D":
            count -= 1
        elif i == "U":
            count += 1
    return(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()