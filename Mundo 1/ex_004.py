"""
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
palavra = input('Digite uma palavra: ')
print(f'Você digitou: {palavra}')
print(f'O tipo primitivo desta palavra é {type(palavra)}')
print(f'Somente tem espaços ? {palavra.isspace()}')
print(f'É um número ? {palavra.isnumeric()}')
print(f'É alfanumérico ? {palavra.isalnum()}')
print(f'É alfabetico ? {palavra.isalpha()}')
print(f'Está em maiúsculas ? {palavra.isupper()}')
print(f'Está em minúsculas ? {palavra.islower()}')
print(f'Está capitalizada ? {palavra.istitle()}')
