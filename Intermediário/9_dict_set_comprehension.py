produto = {
    'nome': 'Kellven Dias',
    'idade': 21,
    'Endereco': "Rua do Pandeiro, 197",
    'Numero': "67992246131"
}

dic1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'Endereco'
}

print(dic1.items())


set1 = {2**i for i in range(10)}
print(set1)