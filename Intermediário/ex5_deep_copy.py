# copy, sorted, produtos.sort
# Exercícios


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {**produto, 'preco': f'{produto['preco']*1.1:.2f}'} for produto in novos_produtos
]

print('Produtos com aumento de 10%:')
print(*novos_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome.sort(
    reverse=True, key=lambda item: item['nome'])

print("Produtos em ordem decrescente: ")
print(*produtos_ordenados_por_nome, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produdos_ordenados_por_preco = copy.deepcopy(produtos)
produdos_ordenados_por_preco.sort(key=lambda item: item['preco'])

print("Produtos ordenados por preço crescente")
print(*produdos_ordenados_por_preco, sep='\n')
