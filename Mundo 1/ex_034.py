"""
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores
a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15% .
"""
sal = float(input('Qual o valor do teu salário: '))

if sal > 1250:
    aumento = sal + (sal * 10 / 100)
    print(f'O teu salário com aumento de 1o% fica R${aumento}')
else:
    aumento = sal + (sal * 15 / 100)
    print(f'O teu salário com 15% de aumento fica R${aumento}')
