#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

#easy 

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here}
    resultadosManzana=0
    resultadosNaranja=0
    arrayPosicionesManzanas=[]
    arrayPosicionesNaranjas=[]
    for i, valor in enumerate(apples):
        arrayPosicionesManzanas.append(a + apples[i])
        
    for j, val in enumerate(oranges):
        arrayPosicionesNaranjas.append(b + oranges[j])
    
        
    for apple in arrayPosicionesManzanas:
        if apple in range(s, t + 1):
            resultadosManzana += 1
    
    for orange in arrayPosicionesNaranjas:
        if orange in range(s, t + 1):
            resultadosNaranja += 1
            
    print(resultadosManzana)
    print(resultadosNaranja)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
