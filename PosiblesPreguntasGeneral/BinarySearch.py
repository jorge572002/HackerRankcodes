"""Dado un array de enteros ordenados y un objetivo, 
realiza una búsqueda binaria para encontrar el índice del objetivo."""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Ejemplo de uso
print(binary_search([1, 2, 3, 4, 5], 4))  # Salida: 3
