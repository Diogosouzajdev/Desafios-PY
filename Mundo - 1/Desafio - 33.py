a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))

#verificando quem é menor
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

 #verificando quem é maior
maior = a
if b > maior:
    maior = b
if c > maior:
        maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))