#Uma classe é uma instância de uma metaclasse

class Foo:
    ...

f = Foo()
print(type(f), isinstance(f, Foo))
print(type(Foo)) #A classe Foo é uma instância da classe 'type'(metaclasse)

#podemos definir uma classe através da metaclasse
Bar = type('Bar', (object,), {})
b = Bar()
print(type(b), isinstance(b, Bar))
print(type(Bar))