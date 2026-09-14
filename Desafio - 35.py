#prguntando cumprimnetos para o usuário
l1 = float(input('Digite o primiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiero lado: '))

#verificando o valor dos lados

if l1 == l2 == l3 :
    print('Equilátero: Todos os lados iguais ')

elif l1 == l2 != l3 :
    print("Isóseles: Dois lados iguais ")
else:
    print('Escaleno:Todos os lados são diferentes ')

