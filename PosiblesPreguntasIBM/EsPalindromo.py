def palindromo (cadena):
    Mayusculas = cadena.upper()
    listaCadena = list(Mayusculas)
    voltear = listaCadena[::-1]
    unir = "".join(voltear)
    if unir == Mayusculas:
        print("es palindromo")
    else:
        print("no es palindromo")



s1="Ana"
s2="pedrO"
palindromo(s1)
palindromo(s2)