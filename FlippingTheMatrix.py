#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    answer = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix[i])//2):
            compareList = [matrix[i][j], matrix[i][(len(matrix)-1)-j],
matrix[(len(matrix)-1)-i][j], matrix[(len(matrix)-1)-i][(len(matrix)-1)-j]]
            answer += max(compareList)
    return(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()