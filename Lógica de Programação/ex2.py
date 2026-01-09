"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = (input('Informe um número: '))
try:
    par = int(numero) % 2 == 0
    if par:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar')
except:
    if type(numero) == float:
        print('O valor informado é do tipo String. Informe um número inteiro')
    elif type(numero) == str:
        print('O valor informado é do tipo String. Informe um número inteiro')
    else:
        print('O valor informado não é do tipo inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int(input('Informe o horário do dia: '))
if horario >= 0 and horario <= 11:
    print(f'Bom dia. São {horario} horas da manhã.')
elif horario > 11 and horario <= 117:
    print(f'Boa tarde. São {horario} horas da tarde.')
else:
    print(f'Boa noite. São {horario} horas da noite.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Informe seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome)>4 and len(nome)<=6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande.')