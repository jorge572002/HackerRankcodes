def fourthBit(number):
# Write your code here
    binario = bin (number)
    string = str (binario)
    reversedst = string[::-1]
    cont = 0
    bits =  0
    for carac in reversedst:
        cont +=1
        if cont == 4:
            bits = int (carac)
    return bits

print(fourthBit(77))