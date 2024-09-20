def multiplos(num, mult):
    return num*mult

print(multiplos(2, 3))
print(multiplos(2, 4))

#Outra solução:

def criar_multiplicador(mult):
    def multiplicador(num):
        return num*mult
    return multiplicador

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2), triplicar(2), quadruplicar(2))

