def voltear(s):
    listaString=list(s)
    volteado=listaString[::-1]
    stringfinal="".join(volteado)
    return stringfinal





s="hola, mundo"
print(voltear(s))