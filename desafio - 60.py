#lendo numero
numero = int(input('Digite um número: '))
original = numero
resultado = 1
while numero > 0:
    resultado *= numero
    numero -= 1
print(f'O fatorial de {original} é {resultado} ')