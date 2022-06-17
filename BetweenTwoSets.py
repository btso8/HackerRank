#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    switch = True
    listOfPot = []
    answer = []
    for val in range(1,min(b)+1):
        for i in a:
            if val % i != 0:
                switch = False
        if switch == True:
            listOfPot.append(val)
        switch = True
    for val in listOfPot:
        for i in b:
            if i % val != 0:
                switch = False
        if switch == True:
            answer.append(val)
        switch = True
    return len(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()