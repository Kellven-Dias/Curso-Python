# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

# def criar_funcao(funcao, *args):
#     return funcao(*args)

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna #deste modo, adiamos a execução para quando houver o fechamento/closure


soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(10))#closure
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(5))#closure