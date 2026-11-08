valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}:' )))
print(f'Voçê digitou os valores {valores}')
maior = max(valores)
menor = min(valores)

print('=' * 30)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
      print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
