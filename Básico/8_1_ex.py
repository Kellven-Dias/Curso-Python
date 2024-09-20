name = input("Digite o seu nome: ")
age = input('Digite sua idade: ')

age = int(age)

if name and age:
    print(f'seu nome e {name}')

    inverted_name = name[::-1]
    print(f'seu nome invertido e {inverted_name}')

    if(' ' in name):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não possui espaços')
    
    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'a última letra do seu nome é {name[-1]}')
else:
    print('Desculpe, voce deixou campos vazios')

