primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ") 

if(primeiro_valor > segundo_valor):
    print(f'primeiro_valor = {primeiro_valor} é maior que segundo_valor = {segundo_valor}')
    
elif(segundo_valor > primeiro_valor):
    print(f'segundo_valor = {segundo_valor} é maior que primeiro_valor = {primeiro_valor}')
else:
    print(f'os dois valores são iguais: primeiro_valor = segundo_valor = {primeiro_valor}')