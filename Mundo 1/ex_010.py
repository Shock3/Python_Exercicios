"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.
"""
real = float(input('Grana: '))
dolar = 5.40 * real
euro = 6 * real
libra = 7 * real
print(f'Com {real}R$ você pode comprar {dolar}$, {euro} e {libra} ')
