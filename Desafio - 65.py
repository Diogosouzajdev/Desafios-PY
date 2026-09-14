n = int(input('Digite um valor: '))
cont = 1
soma = n
maior = n
menor = n
resp = str(input('Quer continuar? [S/N] ')) .upper()
while resp == 'S':
    n = int(input('Digite outro valor: '))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    resp = str(input('Quer continuar? [S/N] ')) .upper()
media = soma / cont
print(f'A média dos valores foi {media:.2f}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')

