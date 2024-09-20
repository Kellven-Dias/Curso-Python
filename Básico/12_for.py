#FOR é usado para iterar coisas finitas

"""
name = 'Kellven Dias'
new_name = ''
for letter in name:
    new_name += f'{letter}-'
print(new_name)

# range(start, stop, step)

numeros = range(0, 21)
numeros_pares = range(0, 22, 2)

for num in numeros_pares:
    print(num)
for num in numeros:
    print(num) 

"""

#Como o for funciona:

name = 'Kellven'
iterador = iter(name) #ou name.__iter()__

#for letra in name:
    #print(letra)

while True:

    try:
        letra = iterador.__next__() #ou next(iterador)
        print(letra)
    except StopIteration:
        break

#for-continue, for-else

for i in range(10):

    if i==5:
        print('Numero cinco encontrado')
        continue
else:
    print('For concluído com sucesso')
