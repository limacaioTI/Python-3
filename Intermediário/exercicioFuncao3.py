# numero = int(input("Digite um número inteiro: "))
# valor = int(input("Digite um valor para multiplicar: "))

# def multiplica(numero, valor):
#     return numero * valor

# resultado = multiplica(numero, valor)
# print(f"O resultado da multiplicação de {numero} por {valor} é: {resultado}")
    

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)
quadruplo = multiplicador(4)

print(dobro(5))      # Saída: 10
print(triplo(5))     # Saída: 15
print(quadruplo(5))  # Saída: 20