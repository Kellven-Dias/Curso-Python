from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

#reduce é usada para aplicar cumulativamente uma funcao a uma seq de elementos, reduzindo-a a um unico valor

soma_dos_precos = reduce(lambda acumula, prod: acumula+prod['preco'],
       produtos,
       0)

print(soma_dos_precos)