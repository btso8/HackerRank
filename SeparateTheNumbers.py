#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
        res = 'NO'
        for i in range(len(s)):
                start = int(s[:i+1])
                newStart = str(start)
                if len(newStart) != len(s):
                        digit = start
                        while len(newStart) < len(s):
                                digit += 1
                                newStart += str(digit)
                        if newStart == s:
                                res = f"YES {start}"
                                break
        print(res)
        

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)