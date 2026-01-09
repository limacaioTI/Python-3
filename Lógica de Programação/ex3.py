nome = 'Caio Lima'

tamanho_nome = len(nome)
contador = 0
 
novo_nome = ''

while contador < tamanho_nome:
    nova_str = nome[contador]
    novo_nome += F'*{nova_str}'
    contador+=1

print(novo_nome)

# Usando for loop
novo_name = ''
for letra in nome:
    novo_name +=f'*{letra}'
print(novo_name)