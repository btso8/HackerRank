#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    answer = 0
    numbers = False
    lower_case = False
    upper_case = False
    special_characters = False
    for char in password:
        if char.isnumeric():
            numbers = True
        elif char.isalpha() and char.islower():
            lower_case = True
        elif char.isalpha() and char.isupper():
            upper_case = True
        elif char in "!@#$%^&*()-+":
            special_characters = True
    if numbers == False:
        answer += 1
    if lower_case == False:
        answer += 1
    if upper_case == False:
        answer += 1
    if special_characters == False:
        answer += 1
    print(n - answer)
    if n + answer < 6:
        answer += 6 - n - answer
    return answer
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()