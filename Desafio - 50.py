cont = 0
soma = 0
for c in range (1,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'Voçê informou {cont} números pares e a soma deles  foi {soma}')
    