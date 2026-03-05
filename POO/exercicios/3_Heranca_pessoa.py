class Funcionario:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome


class Medico(Funcionario):
    def __init__(self, nome, sobrenome, idade, numero):
        super().__init__(nome, sobrenome, idade)  # chama o init da superclasse
        self.numero = numero  # atributo específico


class Psicologa(Funcionario):
    def __init__(self, nome, sobrenome, idade, numero):
        super().__init__(nome, sobrenome, idade)
        self.numero = numero


class Programador(Funcionario):
    def __init__(self, nome, sobrenome, idade, area):
        super().__init__(nome, sobrenome, idade)
        self.area = area
        self.linguagens = []

    def inserir_linguagens(self, *linguagens):
        for linguagem in linguagens:
            self.linguagens.append(linguagem)

    def listar_linguagens(self):
        for linguagem in self.linguagens:
            return linguagem


julia = Psicologa("Julia", "Murteira", "21", "1234543-23")
igor = Medico("Igor", "Sansao", "24", "19283464-23")

caio = Programador("Caio", "Lima", "22", "Software Developer")

l1, l2, l3 = "Python", "SQL", "Java"
caio.inserir_linguagens(l1, l2, l3)

print(
    f"Nome: {julia.nome}\n\
Sobrenome: {julia.sobrenome}\n\
Idade: {julia.idade}\n\
CRM: {julia.numero}"
)

print(
    f"Nome: {igor.nome}\n\
Sobrenome: {igor.sobrenome}\n\
Idade: {igor.idade}\n\
CRM: {igor.numero}"
)

print(
    f"Nome: {caio.nome}\n\
Sobrenome: {caio.sobrenome}\n\
Idade: {caio.idade}\n\
Habilidades: {caio.listar_linguagens()}"
)
