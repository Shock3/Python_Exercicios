"""
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

a = float(input('Comprimento do lado a: '))
b = float(input('Comprimento do lado b: '))
c = float(input('Comprimento do lado c: '))

if a < b + c and b < a + c and c < a + b:
    print('PODE formar um triângulo!')
else:
    print('NÃO PODE formar um triangulo!')
