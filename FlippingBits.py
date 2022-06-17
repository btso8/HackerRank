#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary = bin(n)
    stringN = str(binary[2:])
    stringN = ("0"*(32-len(stringN))) + stringN
    output = ""
    for val in range(32):
        if stringN[val] == "0":
            output += "1"
        else:
            output += "0"
    answer = int(output,2)
    return(answer)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()