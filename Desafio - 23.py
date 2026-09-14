n = int( input('digite um numero: '))

#calculo
unidade = n % 10
dezena = (n// 10) % 10
centena = (n // 100) % 10
milhar = (n// 1000) % 10

print (f'Analisando numero: {n}')
print (f'Unidades {unidade}')
print (f'Dezenas {dezena}')
print (f'Centenas {centena}')
print (f'Milhares {milhar}')