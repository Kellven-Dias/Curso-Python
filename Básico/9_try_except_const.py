num = input("Digite um número: ")

try:
    print(f'voce digitou: {num}')
    num_float = float(num) #Quando ocorrer o erro de uma str no input ele pula para o except

    print(f'o dobro de {num} é {num_float * 2:.1f}')
except:
    print('Você não digitou um número')

#Constantes podem ser definidas em letras maiúsculas:
PI = 3.1415 #constante
pi = 3.14 #variável
