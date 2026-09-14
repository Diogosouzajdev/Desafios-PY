cont = 0
soma = 0
print('Digite 999 para parar')
n = int(input('Digite um valor: '))
while n != 999:
    soma += 1
    cont += 1
    n = int(input('Digite outro valor: '))
print('Foram digitados {} números '.format(cont))
print("A soma dos números é {} ".format(soma))

