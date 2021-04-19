"""
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""
num = int(input('Digite um valor em metros: '))
cent = num * 100  # P/ Centímetros
mm = num * 1000  # P/ Milímetros
dm = num * 10  # P/ Decímetro
dam = num / 10  # P/ Decâmetro
hec = num / 100  # P/ Hectômetro
km = num / 1000  # P/ Quilômetro

print(f'{num} m tem\n{km} km,\n{hec} hm,\n{dam} dam,\n{dm} dm,\n{cent} cm,')
print(f'{mm} mm')
