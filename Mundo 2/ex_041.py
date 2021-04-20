"""
A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
from datetime import date

nasc = int(input('Qual a data de nascimento: '))
data = date.today().year

idade = data - nasc

if idade <= 9:
    print('Categoria Mirim')
elif 14 >= idade > 9:
    print('Categoria infantil')
elif 19 >= idade > 14:
    print('Categoria Júnior')
elif 25 >= idade > 19:
    print('Categoria Sênior')
else:
    print('Categoria Master')
