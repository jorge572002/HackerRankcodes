"""Dado un array de enteros y un objetivo, encuentra dos números en el array 
que sumen el objetivo y devuelve sus índices."""

def two_sum(nums, target):
    num_map = {}  # Diccionario para almacenar el índice de cada número
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Ejemplo de uso
print(two_sum([2, 7, 11, 15], 9))  # Salida: [0, 1]
