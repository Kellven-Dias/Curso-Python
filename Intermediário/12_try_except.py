#Uma boa prática do uso de try e except é definir corretamente os tipos de erros encontrados

while True:
    try:
        saida = 'on'

        a: float = float(input("Digite o primeiro operando: "))
        b: float = float(input("Digite o segundo operando: "))

        potencia: float = a/b

        print(f'{potencia:.2f}\n')
        saida = input("Digite 'S' para sair ou (C) para continuar: ").upper()
        if saida == "S":
            break

    except ValueError as error:
        print(f'Erro: {error.__class__.__name__}')
        print(error)
    except ZeroDivisionError:
        print("Erro: Divisão por zero")
    except Exception:
        print("Erro Desconhecido")

#Try, except, else e finally
#finally executa mesmo que dê algum erro na execução, enquanto o else só executa se nao ocorrer nenhum erro

try:
    #8/0
    8/1
except:
    print("ERRO")
else:
    print("Nao deu erro")
finally:
    print("Finish")

#raise usado para criar exceções:

def divide(a:float, b:float)->float:

    if not isinstance(a, float) or not isinstance(b, float):
        raise TypeError('Os operandos devem ser do tipo float.')

    result: float = a/b


    return print(result)

divide(1,"0")
