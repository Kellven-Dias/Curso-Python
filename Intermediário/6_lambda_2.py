def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y
#esta funcao pode ser definida utilizando lambda:

print(
    executa(
        lambda x, y: x+y, 3, 3
    )
)

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

duplica = executa(
    lambda m: lambda n: n * m,
    5 #precisa passar o primeiro parametro, no caso 5
)
print(duplica(2))
