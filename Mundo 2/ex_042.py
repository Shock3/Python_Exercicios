"""
Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""
a = float(input('Qual o comprimento do lado a: '))
b = float(input('Qual o comprimento do lado b: '))
c = float(input('Qual o comprimento do lado c: '))

if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triângulo')
    if a == b == c:
        print('É um triângulo EQUILÁTERO!')
    elif a == b != c or a != b == c:
        print('É um triângulo ESCALENO!')
    elif a != b != c:
        print('É um triângulo ISÓSCELES!')
else:
    print('Não pode formar um triângulo!')
