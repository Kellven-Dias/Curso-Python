def raiz_enesima(a=1, n=2):
    raiz = a**(1/n)
    print(raiz)

raiz_enesima(64, 3)

def soma(x, y):
    print(x + y)

soma(1, 2) #arg nao nomeado
soma(y=2, x=2) #arg nomeado; independe da ordem da sintaxe da funcao

#para um parametro que pode ou n ser enviado
def soma1(x, y, z=None):
    if z is not None:
        print(x+y+z)
    else:
        print(x+y)

soma1(1, 2)
soma1(1, 2, 3)

#nao posso acessar var de escopos internos
#somente de escopos externos:
x = 5
def escopo():
    print(f'x={x}')
escopo() 
#usando global eu consigo alterar var de escopos internos
def escopo1():
    global x
    x = 55
escopo1()
print(f'x global alterado={x}')

#*args => posso passar vários argumentos(nao nomeados) p funcao, os argumentos são agrupados em 1 tupla
def soma(*args): 
    print(args, type(args))
    soma=0
    for numeros in args:
        soma += numeros
    print(*args)#desempacotando da tupla args
    return soma
    
print(soma(1, 2, 3, 4, 5))
#desempacotar => *numeros

#possivel passar funcoes como parametros, atribuir a uma var:

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa_f(funcao, *args):
    return funcao(*args)

saudacao2 = saudacao

print(executa_f(saudacao, 'Boa noite', 'Bruno'))
print(executa_f(saudacao2, 'Bom dia', 'kellven'))


