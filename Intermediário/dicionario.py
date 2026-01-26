
# pessoa = dict(nome='Jay', sobrenome='Lima)

pessoa = {
    'nome': 'Jay',
    'sobrenome': 'Lima',
    'idade': 5,
    'altura': 1.75,
    'enderecos': [
        {'rua': 'Av Brasil', 'numero': 320},
        {'rua': 'Av Paulista', 'numero': 123}
    ],
}

print(pessoa['nome'])
print(pessoa['enderecos'][0])
print(pessoa['enderecos'])

for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")