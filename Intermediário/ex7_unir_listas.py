
def zipper(lista1, lista2):
    menor = min(len(lista1), len(lista2))
    lista_join = []

    for i in range(menor):
        lista_join.append((lista1[i], lista2[i]))
    return lista_join

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))

#outra solucao

print(list(zip(l1, l2)))


def soma_lista(lista1, lista2):
    menor_indice = min(len(lista1), len(lista2))
    lista_soma = []
    for i in range(menor_indice):
        lista_soma.append(lista1[i]+lista2[i])
    return lista_soma

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

print(soma_lista(l1, l2))

#Outra solucao

lista_soma = [x+y for x, y in zip(l1, l2)]
print(lista_soma)
