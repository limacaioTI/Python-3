numero = int(input("Digite um número inteiro: "))
valor = int(input("Digite um valor para multiplicar: "))

def multiplica(numero, valor):
    return numero * valor

resultado = multiplica(numero, valor)
print(f"O resultado da multiplicação de {numero} por {valor} é: {resultado}")
    