#herdeiros herdam de uma classe mais genérica
#uma classe 'cliente' poder herdar atributos e métodos de uma classe 'pessoa'
#'cliente' extende 'pessoa'
#um objeto É UM outro objeto(este mais genérico geralmente)

#classe principal: super class, base class ou parent class
#classe filhas: sub class, child class, derived class

#pode haver confusao qnd extendemos mts classes filhas
#uma boa prática é criar, geralmente, até 3 níveis

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def id_class(self):
        print(self.nome, self.sobrenome, f' class: {self.__class__.__name__}')

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Kellven', 'Dias')
a1 = Aluno('Vitoria', 'Estevam')

c1.id_class()
a1.id_class()

#podemos usar metodos das classes raiz nas filhas através de super():

class MinhaString(str):
    def upper(self):
        print("CHAMA UPPER DA CLASSE PAI('str')")
        return super().upper()
    
string = MinhaString('ola mundo')
print(string.upper())

#é possível passar parametros para super() para alterarmos o 'ponto de vista':
#Além disso podemos sobrescrever o metodo init para as classes filhas
class A:
    atributo_A = 'A'

    def __init__(self, nomeA):
        self.nomeA = nomeA

    def metodo(self):
        return print('metodo de A')
    
class B(A):
    atributo_B = 'B'

    def __init__(self, nomeA, nomeB):
        super().__init__(nomeA)
        self.nome = nomeB

    def metodo(self):
        return print('metodo de B')
class C(B):
    atributo_C = 'C'

    def metodo(self):
        super().metodo()
        super(B, self).metodo()
        return print('metodo de C')
    
c = C()
print(c.atributo_C)
c.metodo()

a = A('nome em A')
b = B('nome em A', 'nome em B')