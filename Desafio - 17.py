import math
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print(f'A hipotenusa é {hipotenusa:.2f}')