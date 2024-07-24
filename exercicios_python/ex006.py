"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

import math

num = int(input("Digite um número: "))
print(f"""
O dobro de {num} é {num*2}
O triplo de {num} é {num*3}
A raiz quadrada de {num} é {math.sqrt(num)}
""")
