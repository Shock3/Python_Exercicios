"""
Faça um programa que leia três números
e mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
menor = n2

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n2 and n3 < n1:
    menor = n3

print('==' * 10)
print(f'O maior é o {maior} ')
print('==' * 10)
print(f'O menor é o {menor} ')
print('==' * 10)
