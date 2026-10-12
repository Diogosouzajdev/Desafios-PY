#Criar uma tupla com todos os time do brasileirão
clubes = ('Flamengo', 'Palmeiras', 'Athletico - PR', 'Fluminense', 'Bahia', 'Cruzeiro',
          'Atlético - MG', 'Santos', 'Coritiba', 'Bragantino', 'São Paulo', 'Botafogo',
          'EC Vitória', 'Corinthians', 'Mirassol', 'Vasco', 'Grêmio', 'Internacional',
          'Remo', 'Chapecoense')

print(f'Os primeiros 5 times são:', clubes [0:5])
print('='*90)

print('os últimos 4 times são:', clubes[-4:])
print('='*90)
for clube in sorted(clubes):
    print(clube)
print('='*90)
print(f'A chapecoense está na posiçao {clubes.index("Chapecoense")+1}')
