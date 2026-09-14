#Leitura dos numeros

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

#Comparando números

if n1 > n2:
    print(f'O primeiro valor {n1} é maior que o segundo {n2}')
elif n1 < n2:
    print(f'o segundo {n2} valor é maior que o primeiro {n1}')
else:
    print(f'Os valores são iguais {n1} e {n2}')