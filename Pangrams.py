#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    x = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in x:
        if char in alphabet:
            alphabet = alphabet.replace(char,'')
    print(alphabet)
    if len(alphabet) == 0:
        return("pangram")
    else:
        return("not pangram")
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()