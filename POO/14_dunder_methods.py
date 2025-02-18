class Ponto:
    #new cria a instância antes de inicializar
    def __new__(cls):
        instancia = super().__new__(cls)
        print(f'Instância de {cls} criada')
        return instancia
    def __init(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    #para dev's
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'
    #!r -> chama o método __repr__ do objeto com a representação do objeto
    
p1 = Ponto(3, 4)
print(repr(p1))
print(str(p1))    
