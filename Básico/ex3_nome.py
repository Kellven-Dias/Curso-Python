name = input('Digite seu primeiro nome: ')

if (len(name)<=4):
    print('Seu nome é curto')
elif(len(name)>=5 and len(name)<=6):
    print('Seu nome é normal')
elif(len(name)>6):
    print('Seu nome é muito grande')