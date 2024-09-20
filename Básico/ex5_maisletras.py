frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

frase_up = frase.upper()

i=0
max_ocorrencia = 0
letra = ''
ocorrencia = 0
while (i < len(frase_up)):
    
    if(frase_up[i] == ' '):
        i+=1
    
    else:
        letra_atual = frase_up[i]
        ocorrencia = frase_up.count(letra_atual)
    
        if ocorrencia > max_ocorrencia:
            max_ocorrencia = ocorrencia
            letra = frase_up[i]
            i+=1
        else:
            i+=1

print(f'A letra {letra} tem maior ocorrencia na frase com um total de {max_ocorrencia} ocorrencias')