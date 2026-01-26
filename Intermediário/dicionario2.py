pessoa = {}

chave = 'nome'
pessoa[chave] = 'Jay'
# pessoa['sobrenome'] = 'Lima'

print(pessoa[chave])

pessoa[chave] = 'Caio'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print("Chave 'sobrenome' não existe")
else:
    print(pessoa['sobrenome'])