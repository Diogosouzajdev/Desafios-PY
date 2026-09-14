n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média é igual a {}'.format(m))
if m >= 6.0:
    print("Parábens!!, voçê foi aprovado!")
else:
    print("Que Pena, voçê foi reprovado!")
