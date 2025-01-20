#é possivel criar metodos normais (@property, @setter, @classmethod, ...)
#como abstratos, para isso devemos usar @abstractmethod como decorator mais interno
#Foo/Bar : podem ser qlqr coisa
from abc import ABC, abstractmethod

class AbstractFoo(ABC):

    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def name(self):...


    # @name.setter
    # @abstractmethod
    # def name(self, name):...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name
    
    #se eu deixar o decorator de metodo abstrato somente no setter
    #eu preciso colocar o nome da classe antes:
    # @AbstractFoo.name.setter

    @name.setter
    def name(self, name):
        self._name = name
        

foo = Foo('Bar')
print(foo.name)