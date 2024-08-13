"""
En este codigo se nos da un array que tiene una serie de numeros consecutivos y no esta ordenado. 
En el array falta un numero y este debe de ser encontrado

"""

#creamos un función para encontrar ese numero 
def find_missing(input):
    #suma total de los elementos
    actual_sum = sum(input)
    print("resultado de la suma del vector original " + str(actual_sum)+"\n")
    
    #n es el numero de elementos del vector
    n = len(input) + 1
    print("numero de elemnentos del vector "+str(n)+"\n")

    #ahora utilizaremos la formula de la suma aritmetica para series 
    sum_of_elements = (n * ( n + 1 ) ) / 2
    print("suma aritmetica de 1 a n " + str(sum_of_elements)+"\n")
    
    
    #la diferencia entre la suma de los elementos presentes en el vector y la suma aritmetica nos dará el valor faltante
    return int(sum_of_elements - actual_sum)

# Driver code
def main():
    v_list =[2,9,7,8,6,4,1,5,10]
    missing_number = find_missing(v_list)

    print("El numero faltante es: " + str(missing_number))
    
if __name__ == '__main__':
    main()