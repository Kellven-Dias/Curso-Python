#Desempacotamento
#var1, var2, ..., varN = [a1, a2, ..., aN]
#var1 irá receber a1, var2 irá receber a2 e assim por diante.

#queremos pegar somente o primeiro valor:
lista = ['Maria', 'Joao', 'Kellven', 'Eduardo']

name1, *resto_da_lista = lista
print(name1, resto_da_lista)
#usa-se _ para quando eu não irei usar essa variável:
name1, *_ = lista

#queremos o terceiro valor da lista:

_, _, name3, _ = lista
print(name3)

primeiro_nome, *_, ultimo_nome = lista
print(primeiro_nome, ultimo_nome)

#Tupla: lista imutável

names = 'Kellven', 'Vitória', 'Alice'

#names[1] = 'Maria' este código gerará um erro, pois não é possível alterar uma tupla

#converter listas em tuplas e vice-versa:
names2 = tuple(lista)
names3 = list(names2)

#ENUMERAR LISTAS e pegar os índices

lista = ['Kellven', 'Vi', 'Kel', 'Vitória']

for indice, nome in enumerate(lista):
    print(f'[{indice}]', nome)

#printar lista
print(*lista)