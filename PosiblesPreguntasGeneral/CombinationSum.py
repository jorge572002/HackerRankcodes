"""Dado un array de números y un objetivo, encuentra todas las combinaciones
 posibles de números en el array que sumen el objetivo."""


def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], path + [candidates[i]])
    
    result = []
    backtrack(0, target, [])
    return result

# Ejemplo de uso
print(combination_sum([2, 3, 6, 7], 7))  # Salida: [[2, 2, 3], [7]]
