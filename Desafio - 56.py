soma_idades = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0
for c in range(1, 5):
    nome = input('Qual o seu nome: ')
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo: [M/F] ')).strip().upper()

    #soma as idades para calcular a média
    soma_idades += idade

    #atualiza o homem mais velho encontrado
    if sexo == 'M':
        if idade > maior_idade_homem:
           maior_idade_homem = idade
           nome_homem_mais_velho = nome

#conta as mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
media = soma_idades / 4
print(f'A média de idade do grupo é {media} ')
print(f'E {nome_homem_mais_velho} é o homem mais velho')
print(f'E {mulheres_menos_20} mulheres tem menos de 20 anos')

