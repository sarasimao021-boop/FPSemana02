frase = input()
contador = {}

for c in frase:
    if c != " ":  
        contador[c] = contador.get(c, 0) + 1

print(contador)

import re


f1 = re.findall(r'\w+|[^\s\w]', input())
f2 = re.findall(r'\w+|[^\s\w]', input())


comum = set(f2)


resultado = [token for token in f1 if token in comum]


print(" ".join(resultado))