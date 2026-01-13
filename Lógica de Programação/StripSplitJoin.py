frase = ' Olá pessoal, meu nome é Caio. '

lista_frase_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frase_cruas):
    lista_frases.append(lista_frase_cruas[i].strip())

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)