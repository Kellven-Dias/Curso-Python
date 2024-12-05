import copy
#Dicionários 
#Coisas que podem ter atributos
#Chave-Valor: Chave=indice
#As chaves são tipos imutaveis: str, bool, int, float, etc

pessoa = {
    'nome': 'Kellven Dias',
    #'idade': 18,
    'altura': 1.73,
    'sexo': 'M',
    'endereco': [
        {'rua': 'R. Rudy Langassner', 'numero': 99},
        {'rua': 'Rua do Pandeiro', 'numero': 197},
    ],
}

print(pessoa['nome'])
print(pessoa['endereco'])

for chaves in pessoa:
    print(chaves, pessoa[chaves])

#operacoes
pessoa['nome'] = 'Vitoria' #alterar
pessoa['sobrenome'] = 'dos Reis' #criar chave

print(pessoa['nome'], pessoa['sobrenome']) #acessar

#Metodos Uteis
print(pessoa.__len__()) #num de atributos
print(pessoa.keys()) #retorna as chaves
print(pessoa.values()) #retorna os valores
print(list(pessoa.values())) #coloca valores em uma lista. Metodo semelhante p tuplas
print(pessoa.items())#par chave-valor

for chave, valor in pessoa.items():
    print(chave, valor) # pega os valores separados e guarda em var

pessoa.setdefault('idade', 18)
print(pessoa['idade'])

#Copy e shallow copy
d1 = {
    'c1': 10,
    'c2': 20,
    'c3': [1, 2, 3, 4]
}

d2 = d1 #nao copia d1 para d2, mas sim aponta para o mesmo lugar na memoria
#se eu alterar d2 eu alterarei d1:
d2['c1'] = 1000
print(d1['c1'])

#com o copy ele copia para outra var, mas nao faz a copia de valores mutaveis:lista,dic,tuplas,etc.
d2 = d1.copy()
d2['c1'] = 5
d2['c3'][2] = 999
print(d2)
print(d1)

#para fazer um deep copy: import copy e copy.deepcopy()

d2 = copy.deepcopy(d1)
d2['c3'][1]=999
print(d2)
print(d1)
