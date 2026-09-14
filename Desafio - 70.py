print('='*30)
print('LOJA TEM DE TUDO')
print('='*30)

soma = 0
menor = 0
cont = 0
cont1000 = 0
menorproduto = ''
primeiro = True

res = 'S'
while res == 'S':
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o valor do produto: R$ ' ))
    soma += preco
    cont += 1
    if preco > 1000:
        cont1000 += 1
    if primeiro:
        menor = preco
        menorproduto = produto
        primeiro = False
    elif preco < menor:
        menor = preco
        menorproduto = produto
    res = str(input('Quer continuar? [S/N] ')).upper()

    while res != 'S' and res != 'N':
        print('Resposta Invalido')
        res = str(input('Quer continuar? [S/N]' )) .upper()

print('=' * 30)

print(f'O total da compra foi R${soma}')
print(f'{cont1000} produtos custam mais de R$ 1000.00')
print(f'{menorproduto} é o produto mais barato')







