#Leitura do numero inteiro

n = int(input('digite um numero inteiro: '))

#menu de opcoes

print ('''Escolha uma das opções de conversão:'
      [ 1 ] Binário
      [ 2 ] Octal
      [ 3 ] Hexadecimal''')
#escolhendo uma opção

opcao = int(input('sua opcão: '))

if opcao == 1:
    print(f' convertido para binário é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f' convertido para Octagonal é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f' convertido para Hexagonal é igual a {hex(n)[2:]}')
else:
    print('Opçao invalida!')