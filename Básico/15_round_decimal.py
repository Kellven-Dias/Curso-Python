import decimal

num1 = 0.1
num2 = 0.7

sum = num1 + num2

print(sum)#numeros float possuem erro de precisao
print(f'{sum:.2f}')
print(round(sum, 4)) #funcao round() para arredondar

num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')

sum = num1 + num2

print(sum)