import random
print('=' * 40)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 40)
cont = 0
while True:
    n = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    computador = random.randint(0, 10)
    s = n + computador
    if escolha == 'P':
        if s % 2 == 0:
            print('Par')
            print('VOÇÊ GANHOU !!!')
            print('Vamos jogar novamente... ')
            print('=' * 40)
            cont += 1
        else:
            print('Ímpar')
            print('VOÇÊ PERDEU!')
            print('=' * 40)
            break

    if escolha == 'I':
        if s % 2 == 1:
            print('Impar')
            print('VOÇÊ GANHOU !!!')
            print('Vamos jogar novamente... ')
            print('=' * 40)
            cont += 1
        else:
            print('Par')
            print('VOÇÊ PERDEU!')
            print('=' * 40)
            break
print(f'Voçê jogou {n} e o computador {computador}. Total de {s}')
print(f'GAME OVER! Voçê venceu {cont} vezes')




