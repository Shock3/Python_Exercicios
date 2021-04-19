"""
Faça um algoritmo que leia o salário de um funcionário,
e mostre seu novo salário, com 15% de aumento.
"""
print('-=-' * 17)
salario = float(input('Quanto é o teu salário? R$'))
aumento = salario + (salario * 15 / 100)
print(f'Teu salário com 15% de aumento fica R${aumento:.2f}')
print('-=-' * 17)
