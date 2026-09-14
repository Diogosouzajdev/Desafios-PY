n = int(input('Digite um número: '))
cont = 1
primeiro = 0
segundo  = 1
while cont <= n:
    proximo = primeiro + segundo
    print(primeiro)
    primeiro = segundo
    segundo = proximo
    cont += 1
print('FIM')
