v1 = 123
v2 = 123
v3 = 'aa'
#id retorna local na memória
print(id(v1))
print(id(v2))
print(id(v3))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faz tal coisa')
else:
    print('Nao faz tal coisa')

if passou_no_if:
    print('passou pelo if', passou_no_if is not None)
else:
    print('nao passou pelo if', passou_no_if is None)