#Funcoes decoradoras e decoradores
#Decorar = Adicionar / Remover / Restringir / Alterar
#São usados para realizar essas operações antes ou depois de uma funcao
#mas sem mudar a lógica da função

#para varios decoradores, eles são executados de baixo para cima

import time
from functools import lru_cache

def meu_decorador(func):
    def funcao_modificada():
        print("Faz algo antes da execucao da funcao")
        func()
        print("faz algo depois da execucao da funcao")
    return funcao_modificada

@meu_decorador
def minha_funcao():
    print("A funcao original esta sendo executada")

minha_funcao()

#EXEMPLOS DE USO

#Logging 
def log_function_data(func):
    def wrapper(*args, **kwargs):
        print(f'Nome da funcao: {func.__name__}')
        print(f'Argumentos: {args}')
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@log_function_data
def soma(x, y):
    return x+y

soma(3, 5)

#Medição de Desempenho
def timer(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"A funcao {func.__name__} levou {fim-inicio:.8f} segundos para executar")
        return resultado
    return wrapper

@timer
def soma_demorada(n):
    soma = 0
    for i in range(n):
        soma +=i
    return soma

soma_demorada(1000000)

#Cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

#Validação de Argumentos
def validate_digit(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("os Argumentos devem ser numeros inteiros/float")
        return func(*args, **kwargs)
    return wrapper

@validate_digit
def soma_const(*args):
    soma = 0
    for arg in args:
        soma+=arg
    return soma
print(f'A soma é igual a: {soma_const(1, 2, 3)}')
soma_const('a', 2, 3)
