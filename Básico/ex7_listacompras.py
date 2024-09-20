
lista_compras = []
while True:

    
    try:
        command = input('[i]nserir, [a]pagar, [l]istar ou [s]air? ')
        
        command = command.lower()

        if command == 'i':
            produto = input('Digite um produto para ser incluído na lista: ')

            lista_compras.append(produto)
        elif command == 'a':


            """
            indice = input('Digite um índice para ser removido da lista: ')
            indice = int(indice)

            
            present = indice in range(len(lista_compras))
            if present is False:
                print('Digite um índice válido.')
            
            else:
                               
                for i, prod in enumerate(lista_compras):
                    if i == indice:
                        lista_compras.pop(i)
            """
            try:
                indice = input('Digite um índice para ser removido da lista: ')
                indice = int(indice)

                del lista_compras[indice]
            except ValueError:
                print('Digite um numero int')
            except IndexError:
                print('Digite um indice válido')
            except Exception:
                print('Erro desconhecido')
        
        elif command == 'l':
            for i, produtos in enumerate(lista_compras):
                print(i, produtos)

        elif command == 's':
            break
            
        else:
            print('Digite uma opção válida')
    except:
        print('Voce digitou uma opção inválida')