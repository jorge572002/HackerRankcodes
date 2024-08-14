"""Dado un valor y un array de numeros hay que determinar si la sumatoria de dos de los elementos del array dan como resultado el valor establecido
Este es un problema que se puede resolver utilizando hashing si el vector no está ordenado, si está ordenado entonces es posible usar 2 pointers"""
#en este caso no está ordenado
def sum_of_2_int(A,val):
    #Creamos una variable en la cual guadaremos un set vacio
    valores=set()
    #recorremos los valores del arreglo
    for i in A:
        print(i)
        #si el valor de prueba menos el valor del elemento del array se encuentra en el set creado entonces regresas true
        """desarrollando un poco más, cada que el valor resultante de la resta no se encuentre en el set, a este se le añade el valor de (i)
        En la siguiente iteraciones (i) será diferente, nuevamente se intentará la resta y si el valor de la resta se encuentra entre los valores del set que fueron guardados en iteraciones previas,
        eso quiere decir que en efecto existen 2 valores en el array que sumados dan como resutado el valor de prueba. El valor de la resta en la iteración actual más el valor contenido en el set da como resulado una afirmación positiva"""
        if val - i in valores:
            return True
        valores.add(i)
        print(valores)
    return False

v = [5, 7, 1, 2, 8, 4, 3] #array que se va a usar
test = [3, 20, 1, 2, 7] # numeros de prueba 

#loop para usar todos los numeros de prueba
for i in range(len(test)):
    output = sum_of_2_int(v, test[i])
    print("find_sum_of_two(v, " + str(test[i]) + ") = " + str(output))