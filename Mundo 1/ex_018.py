"""
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians


angulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'O seno do ângulo {angulo}° é de {seno:.2f}')
print("--" * 15)
print(f'O Cosseno do ângulo {angulo}° é de {coss:.2f}')
print("--" * 15)
print(f'A tangente do ângulo {angulo} é de {tang:.2f}')
print("--" * 15)
