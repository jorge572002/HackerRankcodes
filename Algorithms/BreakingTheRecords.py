#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    currentmax = scores[0]
    currentmin = scores[0]
    contMin = 0
    contMax = 0
    results = []
    #veces que se rompio el record maximo
    for j in scores:
        if currentmax < j:
            contMax += 1
            currentmax = j
    #veces que se rompio el record minimo 
    for i in scores:
        if currentmin > i:
            contMin += 1
            currentmin = i
    results = [contMax, contMin]
    return results
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
