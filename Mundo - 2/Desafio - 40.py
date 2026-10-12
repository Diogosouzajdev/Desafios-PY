#Leitura de notas
n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))

#Calculo da média
media = (n1 + n2) / 2

#Vericação da nota

if media < 5:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')
print('=' * 20)
print(f'Sua Média foi de {media:.2f}')