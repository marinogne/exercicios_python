#  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

valor_carteira = float(input("Quanto dinheiro você tem na carteira? R$"))
dollar = valor_carteira / 5.63
print(f"Com R${valor_carteira} você pode comprar US${dollar:.2f}")