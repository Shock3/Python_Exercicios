"""
Escreva um programa que converta uma temperatura,
digitando em graus Celsius e converta para graus Fahrenheit.
"""
celsius = int(input('Digite a temperatura: '))
fahrenheit = (celsius / 5) * 9 + 32
Kelvin = celsius + 273
print(f'A temperatura {celsius}°C em Fahrenheit é {fahrenheit}°F')
print(f'E em Kevin fica {Kelvin} K')
