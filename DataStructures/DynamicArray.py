#!/bin/python3

#Easy

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    matriz, lastAnswer, resultado = [[] for _ in range(n)], 0, []
    for i in queries:
        QT, x, y = i[0], i[1], i[2]
        idx = (x ^ lastAnswer) % n
        if QT == 1:
            matriz[idx].append(y)
        elif QT == 2:
            lastAnswer = matriz[idx][y % len(matriz[idx])]
            resultado.append(lastAnswer)
    return resultado

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
