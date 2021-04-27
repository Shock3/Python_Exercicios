"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
IMC = Peso(kg) ÷ (Altura × Altura(m))
"""
massa = float(input('Digite a sua massa corporal: '))
alt = float(input('Digite tua altura: '))
imc = massa / (alt * alt)

if imc < 18.5:
    print('Você está abaixo do peso!')

elif 25 >= imc > 18.5:
    print('Você está com o peso ideal!')

elif 30 >= imc > 25:
    print('Você está com sobrepeso!')

elif 40 >= imc > 30:
    print('Você está Obeso!')

else:
    print('Você está com Obesidade Mórbida!')
