from encodings import search_function

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 0
while cont < 10:
    print(termo)
    termo += razao
    cont += 1
segundo = int(input('Quer mostrar mais algum termo: '))
total = 10 + segundo
while cont < total :
    print(termo)
    termo += razao
    cont += 1