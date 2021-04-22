"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randrange
from time import sleep


print('==' * 15)
print('[1] = PEDRA')
print('[2] = PAPEL')
print('[3] = TESOURA')
print('==' * 15)

player = int(input('Escolha: '))
computer = randrange(1, 4)

if player == 1:
    print('Você escolheu Pedra')
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    if computer == 1:
        print('O cumputador escolheu pedra!')
        print('EMPATOU!')
    elif computer == 2:
        print('O cumputador escolheu Papel!')
        print('Você perdeu!')
    elif computer == 3:
        print('O computador escolheu Tesoura!')
        print('Você ganhou!')

elif player == 2:
    print('Você escolheu Papel')
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    if computer == 1:
        print('O computador escolheu pedra!')
        print('VOCÊ GANHOU!')
    elif computer == 2:
        print('O computador escolheu Papel!')
        print('EMPATOU')
    elif computer == 3:
        print('O cumputador escolheu Tesoura')
        print('O COMPUTADOR GANHOU!')

elif player == 3:
    print('Você escolheu Tesoura')
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    if computer == 1:
        print('O computador escolheu Pedra')
        print('O COMPUTADOR GANHOU')
    elif computer == 2:
        print('O computador escolheu Papel')
        print('VOCÊ GANHOU')
    elif computer == 3:
        print('O computador escolheu Tesoura')
        print('EMPATE')
else:
    print('ERRO! TENTE NOVAMENTE!')
