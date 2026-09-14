l = float(input('Qual a largura da sua parede: '))
a = float(input('Qual a altura da sua parede: '))
m = l * a
print('Então a área da sua parede é : ',m)
area = m / 2
print('então irá precisar de {} litros de tinta ja que cada litro pinta 2m²'.format(area))