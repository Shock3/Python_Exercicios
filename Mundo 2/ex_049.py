"""
Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
"""
print('=-=' * 15)
print('                   TABUADA')
print('=-=' * 15)

num = int(input('Qual tabuada: '))

for c in range(1, 11):
    print(f'{num} X {c} = {num * c}')
