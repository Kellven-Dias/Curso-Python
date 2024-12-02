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