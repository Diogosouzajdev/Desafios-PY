valores = []
for c in range(4):
   num = int (input ('Digite um valor: '))
   valores.append(num)
valores = tuple(valores)
print(f'Voçê digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print('O valor 3 foi digitado pela primeira vez na posição {}'.format(valores.index(3)))
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
num_par = False
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
        num_par = True

if not num_par:
    print('Nenhum número par foi digitado')

