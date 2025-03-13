#Podemos usar funções com trechos de códigos repetitivos para decorar classes

def make_repr(cls):
    def repr(self):
        class_name = self.__class__.__name__ 
        class_dict = self.__dict__
        class_repr = f'{class_name}[{class_dict}]'
        return class_repr
    cls.__repr__ = repr
    return cls

#Podemos usar funções para decorar métodos de classes
#Por exemplo, podemos criar uma função que verifica se o carro é da marca Toyota
#Se for, a função retorna uma mensagem indicando que o carro é da marca Toyota
def my_car(method):
    def intern(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Toyota' in result:
            return 'This is a Toyota'
        return result
    return intern


@make_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@make_repr 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @my_car
    def description(self):
        return f'{self.brand} {self.model}'

#Deste modo, a função make_repr é usada para decorar as classes Person e Car
#Assim, a função repr é adicionada a essas classes

if __name__ == "__main__":
    person = Person('John', 25)
    print(person) #Person({'name': 'John', 'age': 25})
    car = Car('Toyota', 'Corolla')
    print(car) #Car({'brand': 'Toyota', 'model': 'Corolla'})
    print(car.description()) #This is a Toyota
    car = Car('Ford', 'Focus')
    print(car.description()) #Ford Focus
