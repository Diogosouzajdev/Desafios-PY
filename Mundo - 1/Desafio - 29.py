velocidade = int(input('qual a sua velocidade?'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'voçê vai pagar R${multa} de multa por exesso de velocidade')
