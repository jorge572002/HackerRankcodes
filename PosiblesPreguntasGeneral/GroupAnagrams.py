"""Dado un array de cadenas, agrupa las cadenas que son anagramas unas de otras."""

from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    return list(anagrams.values())

# Ejemplo de uso
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Salida: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
