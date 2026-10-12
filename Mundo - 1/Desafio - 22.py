nome  = input ('Qual é o seu nome?')
#nome com todas as letras maiúsculas
print(nome.upper())

#nome com todas as letras minusculas
print(nome.lower())

#remove os espaços e conta o tamanho do resultado
quantidade = (len(nome.replace(' ','')))
print('A quantidade de caractere será: {}'.format(quantidade))

#conta o tamanho do primeiro nome
primeiro_nome = (nome.split()[0])
print('A quantidade de caractere do primeiro nome será: {}'.format(len(nome.split()[0])))