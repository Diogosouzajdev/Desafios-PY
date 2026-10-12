from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8): 
    ano = int( input('Digite o ano do seu nascimento:' ))
    idade = atual - ano
    
    if idade >= 18:
     maior += 1

    else:
     menor += 1
print(f'Das pessoas {maior} são maior de idade')
print(f'Das pessoas {menor} são mneor de idade')
    