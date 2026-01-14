cpf = '169.160.467'

for i in cpf:
    if i not in '0123456789':
        cpf = cpf.replace(i, '')
cpf = list(map(int,cpf))

numerosMultiplicacao1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

tamanhoCpf = len(cpf)
tamanhoMultiplicacao1 = len(numerosMultiplicacao1)
print(tamanhoCpf)
print(tamanhoMultiplicacao1)

noveDigitosCpf = cpf[:9]
tamanhoNoveDigitosCpf = len(noveDigitosCpf)

listaSoma1 = []

for i in range(tamanhoNoveDigitosCpf):
    listaSoma1.append(cpf[i] * numerosMultiplicacao1[i])
print(listaSoma1)

print('Soma dos resultados da multiplicação:')
soma1 = sum(listaSoma1)
print(soma1)

print("Multiplicar o resultado por 10:")
soma1 = soma1 * 10
print(soma1)

print("Obter o resto da divisão por 11:")
resto1 = soma1 % 11
print(resto1)

if resto1 > 9:
    digito1 = 0
else:
    digito1 = resto1
print("O primeiro dígito verificador é:", digito1)

numerosMultiplicacao2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
dezDigitosCpf = noveDigitosCpf + [digito1]
print(dezDigitosCpf)

tamanhoDezDigitosCpf = len(dezDigitosCpf)

listaSoma2 = []

for i in range(tamanhoDezDigitosCpf):
    listaSoma2.append(dezDigitosCpf[i] * numerosMultiplicacao2[i])
print(listaSoma2)

print('Soma dos resultados da multiplicação:')
soma2 = sum(listaSoma2)
print(soma2)
print("Multiplicar o resultado por 10:")
soma2 = soma2 * 10
print(soma2)
print("Obter o resto da divisão por 11:")
resto2 = soma2 % 11
print(resto2)
if resto2 > 9:
    digito2 = 0
else:
    digito2 = resto2

print("O segundo dígito verificador é:", digito2)

cpfFinal = noveDigitosCpf + [digito1, digito2]
cpfFinalStr = ''.join(map(str, cpfFinal))

print("O CPF completo é:", cpfFinalStr)
