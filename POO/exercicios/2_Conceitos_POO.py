class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome_motor):
        self._motor = nome_motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome

    # def __str__(self):
    #     motor_nome = self._motor.nome if self._motor else None
    #     fabricante_nome = self._fabricante.nome if self._fabricante else None
    #     return f'Carro: {self.nome} | Motor: {motor_nome} | Fabricante: {fabricante_nome}'
    
class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0

gol = Carro('Gol')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
gol.fabricante = volkswagen
gol.motor = motor_1_0


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0


print(f'Carro: {fusca.nome} | Fabricante: {fusca.fabricante.nome} | Motor: {fusca.motor.nome}')
print(f'Carro: {gol.nome} | Fabricante: {gol.fabricante.nome} | Motor: {gol.motor.nome}')