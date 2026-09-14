#lendo idade
from datetime import date
ano_nasc = int(input("Qual ano voçê nasceu: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
#idade de alistamento

if idade == 18:
    print('Voçê está na idade para se alistar')
elif idade > 18:
    saldo = idade - 18
    print('voçê pricisa se alistar URGENTIMENTE')
    print(f'Voçê está {saldo} anos atrassado')
else:
    saldo = 18 - idade
    print('Voçê ainda não precisa se alistar')
    print((f'Faltam {saldo} anos para o alistamento '))

