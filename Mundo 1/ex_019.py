"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos
e escrevendo na tela o nome do escolhido.
"""
from random import choice

al1 = input('Nome do primeiro aluno: ')
al2 = input('Nome do segundo aluno: ')
al3 = input('Nome do terceiro aluno: ')
al4 = input('Nome do quarto aluno: ')

lista = [al1, al2, al3, al4]
escolhido = choice(lista)

print(f'O(A) escolhido(a) foi {escolhido}')
