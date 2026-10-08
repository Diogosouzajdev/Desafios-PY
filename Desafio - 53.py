frase =  input('Digite uma frase: ') .upper()
frase = frase.replace(' ', '')
invertida = ''
for c in range(len (frase) - 1, -1, -1):
    invertida += frase[c]
print(f'Frase normal: {frase}')
print(f'Drase invertida: {invertida}')
if frase == invertida:
    print('Temos um políndromo')
else:
    print('A farse digitada não é um polídromo')
    
