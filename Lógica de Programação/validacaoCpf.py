import random

for _ in range(10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * (10 - contador_regressivo_1)
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = 0 if digito_1 > 9 else digito_1

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * (11 - contador_regressivo_2)
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = 0 if digito_2 > 9 else digito_2
    dez_digitos += str(digito_2)
    print(f'CPF gerado: {dez_digitos}')
    