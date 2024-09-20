num1 = input('Digite um número ') 
num2 = input('Digite outro número ')
print('a soma entre eles é', num1 + num2)
print('input() recebe somente strings, por isso precisamos transformar str nos outros tipos')
num1 = int(input('Digite um número ')) #pode gerar erros se o usuário digitar uma str e int(input()) tentar converter uma str em int. Logo, deve-se realizar a conv em outra linha
num2 = input('Digite outro número ')
num2 = int(num2)
print(f'a soma dos numeros é {num1+num2}')