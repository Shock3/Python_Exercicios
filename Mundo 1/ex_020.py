"""
 Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos
 e mostre a ordem sorteada
"""
from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista_nomes = [a1, a2, a3, a4]
shuffle(lista_nomes)

print('A ordem vai ser: ')
print('===' * 20)
print(lista_nomes)
print('===' * 20)
