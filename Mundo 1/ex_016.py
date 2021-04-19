"""
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira.
"""
from math import trunc

num = float(input('Digite um número: '))
inteira = trunc(num)  # could be used int(num)
print(f'O número digitado foi {num} e a porção inteira é {inteira}')
