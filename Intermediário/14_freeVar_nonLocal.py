#Variaveis livres e nonLocals

#Free vars: variaveis que sao usadas em uma funcao, mas que nao e definida nem parametro dessa funcao

def externa():
    x=10
    def interna():
        print(x, interna.__code__.co_freevars) #aqui, a var x é uma var livre, pois está definida na funcao externa
    return interna

closure = externa()
closure()


def concatenar(str_inicial):
    valor_inicial = str_inicial

    def concatenar_com(string=''):

        # valor_inicial += string
        #este trecho de cod acima gera um erro, pois valor_inicial
        #nao pertence ao escopo de "concatenar_com"
        #Frente a isso, devemos fazer:

        nonlocal valor_inicial
        valor_inicial += string
        return valor_inicial
    return concatenar_com

concateno = concatenar("a")
concateno("b")
concateno("c")
print(concateno())
