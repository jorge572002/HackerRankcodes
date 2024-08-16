"""Dada una matriz cuadrada, rota la matriz 90 grados en el sentido de las agujas del reloj."""
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

# Ejemplo de uso
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(matrix)
print(matrix)  # Salida: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
