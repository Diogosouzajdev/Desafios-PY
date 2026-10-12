import random
num = tuple( random.sample(range(0, 10),  5))
print(f'Os valores sorteados foram {num}')
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

