num = input('Digite um numero inteiro: ')

try:
    num_int = int(num)
    if(num_int%2 == 0):
        print(f'{num_int} é um numero par')
    else:
        print(f'{num_int} é um numero impar')
except:
    print('Voce nao digitou um numero inteiro')