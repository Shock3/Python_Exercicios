"""
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão: ')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXA')
esc = int(input('Sua escolha: '))

if esc == 1:
    print(f'{num} convertido para BINÁRIO fica {bin(num)[2:]}')

elif esc == 2:
    print(f'{num} convertido para OCTAL fica {oct(num)[2:]}')

elif esc == 3:
    print(f'{num} convertido para HEXA fica {hex(num)[2:]}')

else:
    print('Opção inválida! Tente novamente!')
