#pergunta quanto recebe
salario = float(input('Digite o seu salario: '))

#opção para quem ganha mais

if salario > 1250:
    novo_salario = salario + (salario * 10 / 100)
    print('Com seu aumento voçê vai receber R${:.2f}'.format(novo_salario))

#opção para quem ganha menos

else:
    novo_salario = salario + (salario * 15 / 100)
    print('Com seu aumento voçê vai receber R${:.2f}'.format(novo_salario))
