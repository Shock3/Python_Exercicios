"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite.
"""
vel = int(input('Qual a velocidade do carro: '))

print(f'Sua velocidade é de {vel}Km/h')
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado por excesso de velocidade!')
    print(f'Você foi multado em R${multa}')
else:
    print('Você está andando no limite de velocidade!')
