"""
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""
print('=-=' * 15)
preço = float(input('Qual o preço do produto? R$'))
desc = preço - (preço * 5 / 100)
print(f'O preço do produto era R${preço}, e com desconto de 5% fica R${desc}')
print('=-=' * 15)
