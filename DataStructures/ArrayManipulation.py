#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

#Hard. Se implementó el metodo de array de diferencias


def arrayManipulation(n, queries):
    
    initial_array = [0 for n in range(n+1)]
    for derecha, izquierda, sumando in queries:
        initial_array[derecha-1] += sumando
        initial_array[izquierda] -= sumando
    temp = 0
    maxnum=0
    for num in initial_array:
        temp += num
        if maxnum < temp:
            maxnum = temp
    return maxnum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
