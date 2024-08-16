"""Dada una cadena, encuentra la longitud de la subcadena más larga sin caracteres repetidos."""

def length_of_longest_substring(s):
    char_map = {}
    start = max_length = 0
    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length

# Ejemplo de uso
print(length_of_longest_substring("abcabcbb"))  # Salida: 3 (subcadena: "abc")
