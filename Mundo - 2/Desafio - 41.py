#leitura do ano de nascimento
from datetime import date
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

#categorias por idade

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Senior')
else:
    print('Senior')
