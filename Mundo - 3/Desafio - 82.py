valores = []
pares = []
impares = []
resp = '[S/N]'
num = ''
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

print('-='*30)

print(f'Lista de todos os valores digitados: {valores}')
print(f'Lista de todos os pares digitados: {pares}')
print(f'Lista de todos os impares digitados: {impares}')
