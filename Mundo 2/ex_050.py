"""
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
num = int(input('Escolha um número: '))

for c in range(num, num + 6):
    if c % 2 == 0:
        soma += c
        print(c, end=', ')
print(f'\nA soma é {soma}')
