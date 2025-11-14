class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #declarar un set para guardar ahi los caracteres
        alreadySeen = set()
        #declarar variables end y start para la ventanta deslizante
        start = 0
        end = 0
        #resultado final
        result = 0

        #ciclo for para recorrer los indices
        for end in range(0,len(s)):
            #mientras que el caracter en la posicion (end) este dentro del set alreadySeen, quitamos el caracter que esta al principio de la ventana (s[start])
            while s[end] in alreadySeen:
                alreadySeen.remove(s[start])
                #incrementamos el indice de inicio de la ventana hasta que ya no "vea" un caracter duplicado
                start += 1
            #fuera del while añadimos el caracter en la posicion del segundo puntero
            alreadySeen.add(s[end])
            
        #actualizar el resultado
            if (end - start + 1) > result:
                result = end - start + 1
        return result
        