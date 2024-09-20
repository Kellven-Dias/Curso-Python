#funções que retornam outras funções

def saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!!'
    return saudar()

s1 = saudacao('Boa noite', 'Bruno')
print(s1)

def saudacao2(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!!'
    return saudar #nao retorna nada, mas salva os dados na memoria

s2 = saudacao2('Boa noite', 'Kellven')
print(s2())#aqui o programa busca na memoria o que foi salvo e retorna o valor

#aqui adiamos a var nome p dentro da função externa p tornar mais dinâmico
def saudacao2(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!!'
    return saudar 

s2 = saudacao2('Boa noite')
print(s2('Kellven Dias'))

#utilização exemplificativa
def saudacao2(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!!'
    return saudar 

falar_boa_noite = saudacao2('Boa noite')
print(falar_boa_noite('Kellven Dias dos Santos'))

