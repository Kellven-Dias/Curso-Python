#criar listas a partir de iteráveis

lista = list(range(10))
print(lista)

#ou usando for:
lista = []
for num in range(10):
    lista.append(num)
print(lista)

#usando list comprehension:
lista = []
lista = [num for num in range(10)]
print(lista)

#possivel fazer operacoes
lista=[]
lista = [num*num for num in range(10)]
print(lista)

#mapeamento de dados em list comprehension

produtos =[
    {'nome': 'Sabao em po', 'preco': 22.00},
    {'nome': 'Detergente', 'preco': 14.50},
    {'nome': 'Agua Sanitaria', 'preco': 17.80},
]

#Para uma promocao de 30% OFF nesses produtos podemos fazer:

produtos_com_desconto = [
    {**produto, 'preco': f'{produto['preco']*0.7:.2f}'}
    for produto in produtos
]

print('Produtos com 30% OFF')
print(*produtos_com_desconto, sep='\n')

print()
#Para um desconto com uma condicao: desconto em prod > 15$:

produtos_com_desconto = [
    {**produto, 'preco': f'{produto['preco']*0.7:.2f}'}
    if produto['preco']>15 else {**produto}
    for produto in produtos
]

print(*produtos_com_desconto, sep='\n')

#filtros = if(sem else) dps do for:
lista=[]
lista = [n for n in range(10) if n%2==0]#filtro p incluir somente pares
print(lista)

#mais de um for
lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))
print(lista)

#fazendo com list comprehension:

lista = []
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(lista)