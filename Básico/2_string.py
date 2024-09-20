
#STRINGS

#escape
print("Kellven \"Dias\"")

#r
print(r"Kellven \"Dias\"")

#concatenacao e repeticao
print('K' * 5)
print('K' + 'E')

#Upper, lower e title
name = 'keLlven dias'
print(name.title())
print(name.upper())
name = 'KELLVEN DIAS'
print(name.lower())

#eliminar espaços em branco
name = 'Kellven   '
name = name.rstrip()
print(name)
name = '         Kellven'
name = name.lstrip()
print(name)

#coments

"""
DOCSTRINGS
n eh comentario. Python lê oq esta escrito porem nao executa nada

"""

#INT e FLOAT

print(1) #int
print(2.99)#float

print( type("Kellven")    ) #classe type retorna o tipo de dado
print( type(.0) )
print(type(.3))
print(.3)

#BOOLEAN
print(10==10)
print(10==3)
print( type(10==10) )

#CONVERSÃO DE TIPOS

print( int('1') + 1)
print( float('1') + 1)
print(bool(''))
print(bool(' '))
print( str(1) + 'b')

#VARIÁVEIS 

kel = 'Kellven'
print(kel)

kel = 10<11
lven = 10>12
print(kel)
print(lven)

#OP
print(10/3)
#Div inteira 
print( 10//3 )

#resto
print( 10%3 )


