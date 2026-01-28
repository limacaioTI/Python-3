perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# print(type(perguntas[1]['Pergunta']))
acertos = 0
   
for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f"{indice}) {opcao}")

    # Reposta vai receber a opção de marcar
    resposta = input('Digite a opção desejada: ')
    resposta = int(resposta)
    if resposta >= 0 and resposta <= len(pergunta['Opções']):
        if pergunta['Opções'][resposta] == pergunta['Resposta']:
            print('Acertou!!!')
            acertos+=1
        else:
            print('Errou!!!')
    else:
        print('A opção escolhida não existe')
print(f"Você acertou {acertos} perguntas.")
