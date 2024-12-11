#verificacao de tipos/classes

def separa_por_tipo(lista: list)->list:

    lista_int = []
    lista_str = []
    lista_de_listas = []
    lista_float = []
    lista_set = []
    lista_dic = []
    lista_others = []


    for valor in lista:

        if isinstance(valor, int):
            lista_int.append(valor)
        
        elif isinstance(valor, str):
            lista_str.append(valor)

        elif isinstance(valor, list):
            lista_de_listas.append(valor)

        elif isinstance(valor, float):
            lista_float.append(valor)

        elif isinstance(valor, set):
            lista_set.append(valor)

        elif isinstance(valor, dict):
            lista_dic.append(valor)

        else:
            lista_others.append(valor)
    return print(lista_others, lista_de_listas, lista_dic, lista_float, lista_int, lista_set, lista_str, sep='\n')


lista = [1, 2, (2, 3), ['a', 'b', 'c'], {'ola', 'mundo'}, {'nome': 'Kellven', 'sobrenome': 'Dias'}, 2.56, 3.72, 'Vitoria dos Reis']

separa_por_tipo(lista)