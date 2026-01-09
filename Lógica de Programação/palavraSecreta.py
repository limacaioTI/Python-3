palavraSecreta = 'Caio'.lower()
secreto = ''
tentativa = 1

tamanhoPalavraSecreta = len(palavraSecreta)

for i in range(tamanhoPalavraSecreta):
    secreto += '*'*tamanhoPalavraSecreta
    
print('*'*tamanhoPalavraSecreta)

while True:
    letra = input('Digite uma letra: ')
    if letra in palavraSecreta:
        letraAcertada = letra
        novoSecreto = ''
        for i in range(tamanhoPalavraSecreta):
            if letraAcertada == palavraSecreta[i]:
                novoSecreto += letraAcertada
            else:
                novoSecreto += secreto[i]
        secreto = novoSecreto
        print(secreto)
        if secreto == palavraSecreta:
            print('Parabéns! Você ganhou!')
            print('Você precisou de', tentativa, 'tentativas.')
            break            
    else:
        tentativa += 1

