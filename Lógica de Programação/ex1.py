nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if len(idade)>0 and len(nome)>0:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    if len(nome)<1:
        print('Você deixou o campo de nome vazio.')
    else:
        print('Você deixou o campo de idade vazio.')