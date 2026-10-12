#Leitura de preço
preco =float(input('informe o valor do produto: '))
print('Opções de pagamento')
print('''1 - Á vista dinheiro / cheque
2 - Á vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais vezes no cartão''')
#Opções de pagamento

opcao = int(input())
if opcao == 1:
    preco = preco - (preco * 0.10)
    print('Voçê vai pagar R$ {:.2f}'.format(preco))
elif opcao == 2:
    preco = preco - (preco * 0.05)
    print('Voçê vai pagar R$ {:.2f}'.format(preco))
elif opcao == 3:
    parcela = int(input('Quantas parcelas 1 ou 2? '))
    print(f'Sua compra foi parcelada em {parcela}x de R${preco / parcela:.2f} sem juros')
    print('Voçê vai pagar R$ {:.2f}'.format(preco))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    preco = preco + (preco * 0.20)
    valor_parcela = preco /parcela
    print('Sua parcela fica em R$ {:.2f}'.format(valor_parcela))
    print('Voçê vai pagar R$ {:.2f}'.format(preco))
else:
    print('Opção invalida')
#Agradecimento
print('Obrigado pela preferêcia Volte sempre!')