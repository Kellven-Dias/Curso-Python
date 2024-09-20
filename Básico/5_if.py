num = input("Digite um número de 0 a 10: ")
num = int(num)

if num<5:
    print('O número é menor que cinco')
elif num==5:
    print('O número é igual a cinco')
elif num>=5 and num<=10:
    print('o número é maior que cinco e menor que 10')
else:
    print('O número é maior que 10')

#Condicao ternária

verifica_par = num%2 == 0
print('O número é par') if verifica_par is True else print('o número é ímpar')
