soma = 0
cont = 0
for c in range(1, 501, 2):
     if c % 3 == 0:
        soma += c
        cont += 1
print(f'Foram encontrados {cont} numeros impares multiplos por tres e a soma deles são :{soma}')