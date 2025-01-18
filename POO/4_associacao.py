#um objeto usa outro objt

class Estudante:

    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta_estudante(self):
        return self._ferramenta
    
    @ferramenta_estudante.setter
    def ferramenta_estudante(self, ferramenta):
        self._ferramenta = ferramenta

class Calculadora:
    def __init__(self, nome):
        self.nome = nome

    def calcular(self):
        return f'{self.nome} está sendo usada para calcular'
    
estudante = Estudante('Kellven')
hp = Calculadora('HP50g')
estudante.ferramenta_estudante = hp

print(hp.calcular())
print(estudante.ferramenta_estudante.calcular())