print('='* 30)
print('DEVBANK')
print('='* 30)

saque = int(input('Qual o valor do saque: R$ '))

nota50 = saque // 50
resto = saque % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota1 = resto // 1

print('=' * 30)
print(f'Total de {nota50} de R$ 50')
print(f'Total de {nota20} de R$ 20')
print(f'Total de {nota10} de R$ 10')
print(f'Total de {nota1} de R$ 1')

print('=' * 30)
print('Volte sempre!')


