palavras = ('estudar', 'python', 'ensinar', 'aprender', 'programar',
            'aula', 'gratis', 'curso', 'lista', 'futuro')
for frase in range(0, len(palavras)):
    print(f'Na palavra {palavras[frase]}, temos ', end='')
    for letra in palavras[frase]:
        if letra in 'aeiou':
         print(letra, end='')
    print()
