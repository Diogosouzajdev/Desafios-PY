quilometro = int(input('Quantos km voçê vai percorrer ? '))
if quilometro <= 200:
    velocidade = quilometro * 0.50
    print('Voçê vai gastar R$ {:.2f}'.format(velocidade))
else:
    velocidade = quilometro * 0.45
    print('Voçê vai gastar R$ {:.2f}'.format(velocidade))