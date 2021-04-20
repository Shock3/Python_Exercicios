"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar ou
se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date


nasc = int(input('Qual seu ano de nascimento: '))
data = date.today().year
idade = data - nasc

if idade == 18:
    print('Você está no ano de alistamento!')

elif idade > 18:
    print('Você ja passou da idade!')
    print(f'Já passou {idade - 18} ano(s)')

else:
    print('Você ainda não está na idade!')
    print(f'Ainda falta(m) {18 - idade} ano(s)!')
