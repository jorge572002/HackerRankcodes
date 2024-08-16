"""Dado un array de enteros y un objetivo, 
determina si hay un subconjunto de la array cuya suma sea igual al objetivo."""
def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

# Ejemplo de uso
print(subset_sum([1, 2, 5], 6))  # Salida: True (subconjunto: [1, 5])
