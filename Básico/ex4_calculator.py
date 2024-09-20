while True:
    
    try:
        operando1 = input('Digite o primeiro operando: ')
        operando1 = float(operando1)
        
        operando2 = input('Digite o segundo operando: ')
        operando2 = float(operando2)
        
        operador = input('Digite o operador(+, -, /, *, **): ')
        result = 0
        
        if(operador == '+'):
            print(f'{operando1} + {operando2} =', operando1+operando2)
        elif(operador == '-'):
            print(f'{operando1} - {operando2} =', operando1-operando2)
        elif(operador == '/'):
            print(f'{operando1} / {operando2} =', operando1/operando2)
        elif(operador == '*'):
            print(f'{operando1} * {operando2} =', operando1*operando2)
        elif(operador == '**'):
            print(f'{operando1} ^ {operando2} =', operando1**operando2)
        else:
            print('Voce nao digitou um operador valido')
        
        
        exit = input('[S]air?: ').lower().startswith('s')
        if exit:
            break
    except:
        print('Voce nao digitou operandos validos')