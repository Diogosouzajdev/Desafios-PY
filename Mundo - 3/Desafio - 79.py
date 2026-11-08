listanum = []
resp = '[S/N]'
n = ' '
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        print('Valor adicionado com sucesso...')
        listanum.append(n)
    else :
        print('Valor duplicado, não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print('=-'*30)
listanum.sort()
print(f'Voçê digitou os valores {listanum}')




