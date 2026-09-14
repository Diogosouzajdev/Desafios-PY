primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 0
while cont < 10:
    print(termo)
    termo += razao
    cont += 1