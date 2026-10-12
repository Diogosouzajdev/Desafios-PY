import random
tentativa = 1
computador = random.randint(0,10)
jogador = int(input('Digite um numero de 0 a 10: '))
while jogador != computador:
    jogador = int(input('Digite um numero de 0 a 10: '))
    tentativa += 1

if jogador == computador:
    print("Parabéns!, Voçê venceu!!!")
print(f'Foram necessárias {tentativa} tentativas: ')