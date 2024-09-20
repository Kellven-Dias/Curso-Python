
#WHILE é usado para iterar coisas finitas ou infinitas
"""
conditional = True
while conditional:
    name = input('Digit your name to continue or "E" for exit: ')
    if name == 'E':
        break
    print(f'Your name is {name}')

conditional = 0

while conditional < 10:
    conditional += 1

    if (conditional%2 == 0):
        continue

    print(conditional)
"""
#while + while

"""
qntd_linhas = 5
qntd_colunas = 5
linha = 1
while linha <= qntd_linhas:
    coluna = 1
    
    while coluna <= qntd_colunas:
        print(f'L{linha} C{coluna}')
        coluna+=1
    linha+=1
"""

#separar letras str
name = 'Kellven Dias'
name_sep = ''
count = 0

while (count < len(name)):
    name_sep += f'{name[count]}-'
    count+=1

print(name_sep)