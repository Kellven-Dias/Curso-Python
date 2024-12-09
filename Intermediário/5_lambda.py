#funcao lambda
#escrita em uma linha apenas

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#ordenacao por nome usando uma funcao convencional
def ordena(item):
    return item['nome']

lista.sort(key=ordena)
for item in lista: print(item)

print()
print()

#ordenacao usando a funcao lambda  

lista2 = [
    {'nome': 'Kellven', 'sobrenome': 'dias'},
    {'nome': 'Vitoria', 'sobrenome': 'Estevam'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

lista2.sort(key=lambda item: item['nome'])
for item in lista2: print(item)

print()
print()
#ordenar por sobrenome (ordenacao de acordo com tabela unicode utf8 dos caracteres)
lista2.sort(key=lambda item: item['sobrenome'])
for item in lista2: print(item) 