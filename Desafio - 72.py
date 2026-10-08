#Criar a tupla com todos os numeros por extenso de 0 a 20
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Escolha um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
    print('Tente novamente ', end='')

#mostrar numero correspondenteda tupla
print('-'*30)
print(f'Voçê escolheu o número: {cont[num]}')

