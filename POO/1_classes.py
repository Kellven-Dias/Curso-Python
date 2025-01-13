#Classes possuem atributo e metódos
#Objetos são instancias de classes
#init(construtor) inicializa atributos da classe
#Classes representadas por PascalCase
#Uma classe é como se fosse um molde para criacao de objetos

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self): #metodo
        print(f'{self.nome} está falando')

    #metodos de classes: sem a instancia
    @classmethod
    def sobrenome_dias(cls, nome):
        return cls(nome, 'Dias')

p1 = Pessoa("Kellven", "Dias")
p2 = Pessoa("Vitoria", "Estevam")
p3 = Pessoa.sobrenome_dias("Wanilza")

print(p1.nome, p1.sobrenome)
p1.falar()

#__dict__ ou vars mostra o dicionário com os dados dos objetos
print(p1.__dict__)
print(vars(p2))