"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print('==' * 20)
print('                Lojinha')
print('==' * 20)
produto = float(input('Qual o preço do produto? R$'))
print('Temos as seguintes opções de pagamento: ')

print('===' * 20)
print('[1] À vista dinheiro/cheque - desconto de 10%')
print('[2] À vista no cartão - desconto de 5%')
print('[3] Em até 2x no cartão - preço normal')
print('[4] 3x ou mais no cartão - juros de 20%')
print('===' * 20)
form_pag = int(input('Qual a forma de pagamento: '))

if form_pag == 1:
    preço = produto - (produto * 10 / 100)
    print(f'O preço do produto ficou por R${preço:.2f}')

elif form_pag == 2:
    preço = produto - (produto * 5 / 100)
    print(f'O preço do produto ficou por R${preço:.2f}')

elif form_pag == 3:
    print(f'Você pagará o preço normal do produto. R${produto:.2f}')

elif form_pag == 4:
    preço = produto + (produto * 20 / 100)
    print(f'O preço do produto ficou por R${preço:.2f}')
else:
    print('Forma de pagamento não reconhecida! Tente novamente!')
