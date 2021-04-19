"""
Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e raiz quadrada.
"""
from math import sqrt

num = int(input('Digite um número: '))
print(f'O dobro desse número é: {num*2} \nO triplo desse número é: {num*3}')
print(f'A raiz quadrada desse número é: {sqrt(num):.3f}')
