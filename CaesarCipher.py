#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ""
    for i in range(len(s)):
        if (s[i].isupper()):
            result += chr((ord(s[i]) + k - 65) % 26 + 65)
        elif (s[i].islower()):
            result += chr((ord(s[i]) + k - 97) % 26 + 97)
        else:
            result += s[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()