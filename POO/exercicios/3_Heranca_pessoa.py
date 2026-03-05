class Funcionario:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

class Medico(Funcionario):
    def __init__(self, numero):
        self.numero = numero

class Psicologa(Funcionario):
    def __init__(self, numero):
        self.numero = numero

julia = Funcionario("Julia", "Murteira", "21")
crp = Psicologa("123456789")
julia.crp = crp


igor = Funcionario("Igor", "Sansao", "24")
crm = Medico("2856436")
igor.crm = crm

print(
    f"Nome: {julia.nome}\n\
Sobrenome: {julia.sobrenome}\n\
Idade: {julia.idade}\n\
CRM: {julia.crp.numero}"
)

print(
    f"Nome: {igor.nome}\n\
Sobrenome: {igor.sobrenome}\n\
Idade: {igor.idade}\n\
CRM: {igor.crm.numero}"
)
