valores = []
resp = '[S/N]'

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break

print('=-'*30)
print(f'Foram digitados {len(valores)} elementos na lista!')
valores.sort(reverse=True)
print(f'Os valores em forma decrescente são {valores}')
if 5 in valores:
    print('O valor 5 apareceu na lista!')
else:
    print('O valor 5 não foi adicionado na lista!')