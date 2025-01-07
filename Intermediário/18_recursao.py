#toda funcao recursiva deve ter:
#- um problema que possa ser dividido em partes menores
#- um caso recursivo que resolve o pequeno problema
#- um caso base para parar a recursao

def fatorial(n):
    
    if n == 0 or n==1:#casos bases
        return 1
    return n*fatorial(n-1)
    
print(fatorial(5))