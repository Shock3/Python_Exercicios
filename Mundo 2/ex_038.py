"""
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

maior = n1

if n1 > n2:
    maior = n1
    print(f'O número {maior} é o maior!')
    print(f'O numero {n2} é o menor!')

if n2 > n1:
    print(f'O número {n1} é o menor')
    print(f'O numero {n2} é maior ')

elif n1 == n2:
    print('Eles são iguais!')
