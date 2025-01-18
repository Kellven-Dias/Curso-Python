#composicao é uma especialização da agregação
#os objetos relacionados precisam estar juntos
#se excluir o pai, todas as ref serão apagadas também
#um objeto E DONO DE outro objeto
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua , numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero, sep=', ')

    def __del__(self):
        print("Apagando", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("Apagando: ", self.rua, self.numero)
        
c1 = Cliente("Kellven")
c1.inserir_endereco('Rua do Pandeiro', 197)
c1.inserir_endereco('R. Rudy Langassner', 99)
c1.listar_enderecos()

#se eu apagar um cliente a relacao de composicao faz com que os
#enderecos do cliente sejam tb apagados:

del c1

