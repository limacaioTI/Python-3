from pessoa import Pessoa
from contas import Conta

class Cliente(Pessoa, Conta):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade, conta)