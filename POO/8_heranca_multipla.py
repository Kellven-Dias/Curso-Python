#herança multipla: um objeto herdar mais de uma classe mãe
#problema do diamante: se uma classe filha extende duas classes mães que possuem
#metodos com nomes iguais, qual ela ira executar?

#Para saber a ordem da chamadas dos metodos usamos Classe.mro() ou __mro__

class A:
    def who(self):
        print('A')

class B(A):
    
    def who(self):
        print('B')

class C(A):

    def who(self):
        print('C')

class D(B, C):

    ...
    #def who(self):
        #print('D')

d = D()
d.who()
print(D.mro())