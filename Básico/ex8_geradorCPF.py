
import re
import sys
import random

try:

    cpf = '868.372.282-13'#input('Digite um número de CPF(xxx.xxx.xxx-xx): ')

    """
    nove_digitos = cpf[0:11].replace('.', '').replace('-', '').replace(' ', '')
    print(nove_digitos)
    num_cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    print(num_cpf)
    """

    cpf = re.sub(r'[^0-9]', '', cpf) #substitui qualquer coisa q nao for número por ''
    
    #gerar cpf's
    nove_digitos =''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))
    



    num_cpf = re.sub(r'[^0-9]', '', cpf)
    #print(num_cpf)


    #entrada repetida
    primeiro_caractere = cpf[0]
    if cpf == primeiro_caractere*len(cpf):
        print(f'Cpf {cpf} é inválido')
        sys.exit()


    regressive = 10
    sum = 0
    #count = 0

    for digitos in nove_digitos:
        sum += regressive*int(digitos)
        regressive-=1

    """
    while regressive>=2:
        sum += regressive*int(numbers[count])
        count+=1
        regressive-=1
    """
    
    #multiplicar resultado por 10
    sum*=10
    #pegar resto da div por 11
    sum%=11

    first_digit = sum if sum<=9 else 0
    #print(first_digit)

    dez_digitos = nove_digitos+str(first_digit)
    
    regressive = 11
    sum=0
    for digito in dez_digitos:
        sum += regressive*int(digito)
        regressive-=1

    #print(sum)
    sum = (sum*10)%11

    second_digit = sum if sum<=9 else 0
    #print(second_digit)


    cpf_valido = dez_digitos+str(second_digit)
    print(cpf_valido)

    print('CPF válido!') if cpf_valido==num_cpf else print('CPF inválido!')

except:
    print('Erro inesperado')