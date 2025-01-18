
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        return print(self.nome)

class Motor:
    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        return print(self.nome)

if __name__ == '__main__':

    fusca = Carro('Fusca')
    motor_boxer = Motor('Boxer')
    volkswagen = Fabricante('Volkswagen')

    fusca.motor = motor_boxer
    fusca.fabricante = volkswagen

    print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome, sep='/')

    palio = Carro('Palio')
    motor_etorq = Motor('Fiat E-Torq')
    fiat = Fabricante('Fiat')

    palio.motor = motor_etorq
    palio.fabricante = fiat

    print(palio.nome, palio.motor.nome, palio.fabricante.nome, sep='/')

    
