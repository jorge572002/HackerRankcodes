def minMax(arr):
    maximo=arr[0]
    minimo=arr[0]
    for valormax in arr:
        if valormax > maximo:
            maximo = valormax

    for valormin in arr:
        if valormin <  minimo:
            minimo = valormin
    return minimo, maximo


arr=[8, 0, 1, 5, 3, 4, 2, 6]
print(minMax(arr))