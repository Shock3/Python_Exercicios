"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
 Calcule e mostre o comprimento da hipotenusa
"""
from math import sqrt


print('---' * 17)
cat_op = int(input('Comprimento do cateto oposto: '))
cat_ad = int(input('Comprimento do cateto adjacente: '))
hipo = sqrt(cat_ad**2 + cat_op**2)
print(f'O comprimento da hipotenusa é de {hipo:.1f}m')
print('---' * 17)
