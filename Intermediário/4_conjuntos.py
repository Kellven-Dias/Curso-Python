#conjuntos (set)
#mutável, mas so pode ter elementos imutaveis: str, tuplas, bool, int, ...
s1 = set() #vazio
s2 = {'Kellven', 1, 2, 24}
print(s2, type(s2))

#nao garantem ordem
#nao tem indexes
#pode ser iteravel com for, while, etc
#remover elementos repetidos:

lista1 = [1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]
lista2 = list(set(lista1))
print(lista2)

#metodos
s1.add('Dias')
print(s1)

s1.update(("Kellven Dias", 1))
print(s1)

s1.clear() #limpa

s1.add(1)
s1.add(2)
s1.discard(1) #retira do set
print(s1)

s2 = {1, 2, 3}
s3 = {2, 3, 4}

uniao = s2|s3 #uniao
intersecao = s2 & s3 #intersecao
diferenca = s2 - s3 #diferenca
dif_simetrica = s2^s3 #diferenca simetrica

print(uniao, intersecao, diferenca, dif_simetrica)

