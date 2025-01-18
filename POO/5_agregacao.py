#agregacao é um tipo de associação
#os objetos relacionados pela agregacao geram mais valor quando estao agregados
#ex: carrinho de compras e produtos
#os dois podem existir sozinhos, mas juntos fazem mais sentido
#um objeto TEM outro obj
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Regua', 23.57), Produto('Caneta', 7.00)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())