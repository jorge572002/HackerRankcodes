#!/bin/python3

import math
import os
import random
import re
import sys

#medium


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    resultados=[]
    frecuencia={} #necesita ser un diccionario para que se le asigne un valor numerico a cada elemento str
    
    #primer contamos la frecuencia con la que apariencia los datos en stringList
    for i in stringList:
        if i in frecuencia:
            frecuencia[i] += 1
        else:
            frecuencia[i] = 1
            
    for j in queries:
        if j in frecuencia:
            resultados.append(frecuencia[j])
        else:
            resultados.append(0)
            
    return resultados            
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
