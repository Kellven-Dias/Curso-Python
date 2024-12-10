#empacotamento e desempacotamento em dicionarios

pessoa = {
    'nome': 'Kellven',
    'sobrenome': 'Dias',
}

(a1, a2), (b1, b2) = pessoa.items() #com isso eu desempacoto as chaves e os valores
print("ex1:", a1, a2)
print("ex1:", b1, b2)

a, b = pessoa.values() #desempacoto os valores
print("ex2:", a, b)

#pode ser feito usando for

print("ex3:")
for chave, valor in pessoa.items():
    print(chave, valor)


dados_pessoa = {
    'idade': 21,
    'altura': 1.73,
}

pessoa_com_dados = {**pessoa, **dados_pessoa, 'sexo': 'M',}
print(pessoa_com_dados)

#*args = argumentos não nomeados
#**kwargs = argumentos nomeados (keywords argument)

def mostra_argumentos(*args, **kwargs):
    print("Arg n nomeados: ", args)
    print("Arg nomeados: ", kwargs)

mostra_argumentos(1, 2, 'Kellven', sobrenome='dias', idade=25)
print()
mostra_argumentos(**pessoa_com_dados)

