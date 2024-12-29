from itertools import combinations, permutations, count, product, groupby

#Count é um range sem fim e é um iterator
#tem steps e start: count(start=10, step=2)
for i in count():
    print(i)
    if i == 10:
        break

l1 = ['Kellven', 'Vitória', 'João', 'Maria', 'Felipe']

def print_itr(iterator):
    print(*list(iterator), sep='\n')
    print()

print_itr(combinations(l1, 2))#combinacao a ordem nao importa, então (Kellven e Vitoria) e (Vitoria e Kellven)
#nao possui diferenca

print_itr(permutations(l1, 2))#permutacao a ordem importa

l2 = [
    ['preta', 'branca', 'azul'],
    ['P', 'M', 'G']]

#produto cartesiano
print_itr(product(product(*l2)))

#GROUPBY - agrupando por valores
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_agrupados = sorted(alunos, key= lambda item: item['nota'])
# print(*alunos_agrupados, sep='\n')
grupos = groupby(alunos_agrupados, key= lambda item: item['nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno['nome'])
print()



#MAP = primeiro parametro é uma funcao e o segundo é um iterável
precos = [10, 15.5, 12.67, 13, 27.80]

precos_10porcento_off = list(map(lambda x: round(x*0.9, 2), precos))
print(*precos_10porcento_off, sep='\n')
print()
#FILTER

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

filtrar_ate_50reais = filter(lambda p: p['preco']<50, produtos)
print(filtrar_ate_50reais)#filter object
filtrar_ate_50reais = list(filtrar_ate_50reais)
print(*filtrar_ate_50reais, sep='\n')