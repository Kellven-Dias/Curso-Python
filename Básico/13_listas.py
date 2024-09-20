"""
lista = [12, 'Kellven Dias', [], 1.23422]
print(lista)
print(lista[2], type(lista[2]))

lista = [2, 3, 7, 8]
del lista[2] #dispendioso pois consome muito ao re-organizar os elementos
print(lista) 

lista.append(30) #adiciona no final
print(lista)

lista.pop() #remove ultimo elemento ou pode ser passado o indice lista.pop(2)
print(lista)

lista.insert(0, 77) #insert(posicao, elemento a ser add)
print(lista)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_d = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_d, lista_a)

lista_c = lista_a
lista_e = lista_a.copy()
lista_a[0] = 'K'

#lista_c aponta para o mesmo espaço da memoria que a lista_a, portanto se alterarmos a lista_a alteraremos a lista_c
#lista_e faz uma cópia da lista_a, mesmo que alteremos lista_a, não alteramos a lista_e
print(lista_c, lista_e)

#FOR pode percorrer listas

for num in lista_a:
    print(num)

#exercicio
lista = ['Maria', 'Helena', 'Luiz']
count = 0
for nome in lista:
    print(nome, f'[{count}]')
    count+=1

indices = range(len(lista))

for i in indices:
    print(i, lista[i])

#Listas dentro de listas


lista = [[1, 2, 3], ['Maria', 'Joao', 'Vitoria'], [23]]
print(lista[0][2])
print(lista[1][2])