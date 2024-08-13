#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    horaCorta=s[:-2]
    num=horaCorta.split(":")
    lista_de_numeros = [int(x) for x in num]
    if "PM" in s and lista_de_numeros[0] != 12:
        lista_de_numeros[0] += 12
    elif "AM" in s and lista_de_numeros[0] == 12:
        lista_de_numeros[0] = 00
    
    cadena = "{:02}:{:02}:{:02}".format(lista_de_numeros[0], lista_de_numeros[1], lista_de_numeros[2])
    return cadena

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
