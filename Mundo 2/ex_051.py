"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('=-=' * 20)
print('                    Progressão Aritmética')
print('=-=' * 20)

priTermo = int(input('Escolha o primeiro termo: '))
razao = int(input('Escolha a razão da PA: '))
decTermo = priTermo + (11 - 1) * razao  # an = a1 + (n-1) x r

for pa in range(priTermo, decTermo, razao):
    print(pa, end=' -> ')
print('END')
