
class Caneta:

    def __init__(self):
        self._cor = None
        self._cor_tampa = None


    @property #getter
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

c1 = Caneta
c1.cor = 'Vermelha'
print(c1.cor)