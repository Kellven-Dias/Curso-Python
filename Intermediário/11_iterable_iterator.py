#O iterator produz um valor por vez atraves de __next_()

import sys

iterable = [1, 2, 3, 4, 5]
iterator = iterable.__iter__()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator)) #neste print o iterator retorna um erro, pois acabou os elementos

#Generator: "lista" que pausa. Diferentemente de uma lista, o generator n salva todos os seus elementos
#de uma vez so na memoria mas, salva um por um:

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista), sys.getsizeof(generator)) #aqui, vemos que a lista ocupa um espaço mt maior que o generator, pois armazena
#todos os valores de uma vez so na memoria
#generator nao possui tamanho nem indice

#Generator Functions: funcoes que podem pausar:

def generator(n=0, max=10):
    
    while True:
        yield n #a instrucao yield faz a pausa do generator
        n+=1

        if n>=max:
            return "FIM"
        
gen = generator(max=10)
#for i in gen:
    #print(i)

#outro exemplo:

def generator2(n=0, max=10):
    yield 1

    yield 2

    yield 5


gen2 = generator2(0, 10)
print(next(gen2))
print(next(gen2))
print(next(gen2))
print()

#instrucao yield from pode ser usada para continuar da onde outro generator parou:

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5

gen = gen2()
for i in gen:
    print(i)
