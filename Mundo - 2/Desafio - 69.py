#Contadores
maior18 = 0
homens = 0
mulheres20 = 0

print('-' * 40)
print('CADASTRO')
print('-' * 40)

res = 'S'

#Cadastro de pessoas
while res == 'S':

    #sexo
    sexo = str(input('Qual o seu sexo: [M/F]')) .upper()

    while sexo != 'M' and sexo != 'F':
        print('Sexo Invalido')
        sexo = str(input('Qual o seu sexo: [M/F]: ')).upper()

    #Idade
    idade = int(input('Qual a sua idade: '))

    #Contagem
    if idade > 18:
        maior18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    print('-' * 40)

    #Continuar
    res = str( input('Quer continuar? [S/N]')).upper()

    print('-' * 40)

    while res != 'S' and res != 'N':
        print('Resposta Invalido')
        res = str(input('Quer continuar? [S/N]' )) .upper()

print('-' * 40)
#Resultado

print(f'{maior18} pessoas tem mais de 18 anos.')
print(f'{homens} homens cadastrados.')
print(f'{mulheres20} mulheres com menos de 20 anos.')








