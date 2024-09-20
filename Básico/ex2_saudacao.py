hora = input('Informe o valor das horas(excluindo os minutos): ')

try:
    hora = int(hora)


    if (hora <= 11 and hora>=0):
        print('Bom dia')
    elif(hora<=17 and hora>=12):
        print('Boa tarde')
    elif(hora<=23 and hora>=18):
        print('Boa noite')
    else:
        print('Voce nao digitou uma hora válida') 
except:
    print('Voce nao digitou um numero valido')