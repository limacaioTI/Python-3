class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self._id = None

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self._cod = None

    @property
    def cod_func(self):
        return self._cod
    
    @cod_func.setter
    def cod_func(self, valor):
        self._cod = valor

class Atendente(Funcionario):
    def __init__(self, nome, sobrenome, cod, cargo):
        super().__init__(nome, sobrenome)
        self.cod_func = cod
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, sobrenome, cod, filial):
        super().__init__(nome, sobrenome)
        self.cod_func = cod
        self.filial = filial

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, id):
        super().__init__(nome, sobrenome)
        self._id = id
    
    @property
    def id_cliente(self):
        return self._id
    
    @id_cliente.setter
    def id_cliente(self, valor):
        self._id = valor

joao = Atendente("Joao", "Silva", 6749, "Atendente Geral")

carlos = Gerente("Carlos", "Cunha", 9836, "Niteroi")

lucas = Cliente("Lucas", "Santos", 4590456314)

print(f"Nome: {joao.nome}\nSobrenome: {joao.sobrenome}\n")