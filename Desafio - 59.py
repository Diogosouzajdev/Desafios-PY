n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('========')
    print ('MENU')
    print('========')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] Sair')
    opcao = int(input('Qual sua opcao: '))
    if opcao == 1:
        numero1 = n1 + n2
        print(f'A soma entre {n1} e {n2} é iguak a {numero1}')
    elif opcao == 2:
        numero1 = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {numero1}')
    elif opcao == 3:
        numero1 = max(n1, n2)
        print(f'O maior entre {n1} e {n2} é {numero1}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else :
        print('Sair')

