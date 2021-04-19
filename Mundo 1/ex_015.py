"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado
"""
print('**' * 19)
distancia = int(input('Qual a distância percorrida: '))
dias = int(input('Quantos dias ficou alugado: '))
preço = (60 * dias) + (0.15 * distancia)
print(f'O preço total a pagar é de R${preço:.2f}')
print('**' * 19)
