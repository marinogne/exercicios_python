#  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = int(input("Digite um valor em metros: "))
cm = valor*100
mm = valor*1000
print(f"""A medida de {valor}m é igual a {cm}cm e {mm}mm.""")