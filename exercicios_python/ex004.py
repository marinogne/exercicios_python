"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

algo = input("Digite algo: ")
print(f'O tipo primitivo é {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em MAIÚSCULO? {algo.isupper()}')
print(f'Está em minúsculo? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')