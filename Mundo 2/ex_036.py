"""
Aula 012 - Condições aninhadas
Faça um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. A prestação mensal
não pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('=' * 80)
print('                              BANCO BRASILEIRO')
print('=' * 80)

sal = float(input('Qual o valor do teu salário R$'))
casa = float(input('Qual o valor da casa R$'))
anos = int(input('Em quantos anos pretende pagar: '))


sal_percent = sal * 30 / 100
parcelas = anos * 12
prestação = casa / parcelas

if prestação >= sal_percent:
    print(
        f'A prestação fica R${prestação:.2f}, é mais que 30% do teu salário!')
    print('Emprestimos NEGADO')
else:
    print('Empréstimo APROVADO')
    print(f'O valor das parcelas fica R${prestação:.2f} por {parcelas} meses')
