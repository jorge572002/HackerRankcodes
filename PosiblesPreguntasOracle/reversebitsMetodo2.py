def reverse(decimal):
    binario=bin(decimal)
    listabin=list(binario)
    num=listabin[2:]
    reverse=num[::-1]
    print(int("".join(reverse)))



reverse(362)