import random

computador = random.randint(0,5)
jogador = int(input('Digite um numero de 0 a 5: '))

if jogador == computador:
    print("Parabéns!, Voçê venceu!!!")
else:
    print("Que pena, eu nao pensei nesse numero ")
    print(f"O eu escolhi o número {computador}")