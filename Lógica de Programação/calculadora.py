
condicao = True

while condicao:
    num1 = input('Digite o número 1: ')
    num2 = input('Digite o número 2: ')
    operador = input('Informe o operador desejado (+,-,*,/)')

    num1_float = 0.0
    num2_float = 0.0

    if num1.isdigit() and num2.isdigit():
        
        try:
            num1_float = float(num1)
            num2_float = float(num2)
        except:
            print('O valor enviado não é do tipo float')
        
        if operador == '+':
            print(f'{num1_float} + {num2_float} = ', num1_float+num2_float)
        elif operador == '-':
            print(f'{num1_float} - {num2_float} = ', num1_float-num2_float)
        elif operador == '*':
            print(f'{num1_float} * {num2_float} = ', num1_float*num2_float)
        elif operador == '/':
            print(f'{num1_float} / {num2_float} = ', num1_float/num2_float)
        
        else:
            ...

        opcao = input('Deseja [s]air? ').lower()

        if opcao == 's':
            condicao = False
        else:
            continue
            
    else:
        print('Digite um valor adequado.')