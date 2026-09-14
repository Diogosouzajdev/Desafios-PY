import math
an = float(input("digite o valor do ângulo: "))
rad = math.radians(an)
seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)

print(f'O valor do seno: {seno:.2f}')
print(f'O valor do coseno: {coseno:.2f}')
print(f'O valor da tangente: {tangente:.2f}')
