import os
import json

def listar(tarefas):
    if not tarefas:
        print("Não há tarefas para listar")
        return

    print("TAREFAS:")
    for t in tarefas:
        print(f'\t -{t}')

def desfazer(tarefas, tarefas_desfazer):
    if not tarefas:
        print("Não há tarefas para desfazer")
        return

    tarefas_desfazer.append(tarefas.pop())
    return listar(tarefas)

def refazer_tarefas(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print("Não há tarefas para refazer")
        return
    
    tarefas.append(tarefas_refazer.pop())
    return listar(tarefas)

def limpar(tarefas):
    tarefas.clear()
    print("Lista de tarefas limpa!")
    return listar(tarefas)

def limpar_console():
    print("\n" * os.get_terminal_size().lines)

def adicionar(tarefa, tarefas):
    print(f'"{tarefa}" adicionada à lista de tarefas')
    tarefas.append(tarefa)



def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    
    except FileNotFoundError:
        print("Arquivo nao existe")
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
        return dados


CAMINHO_ARQUIVO = "Intermediário\\ex8_salvar_tarefas.json"
tarefas = ler([], CAMINHO_ARQUIVO)
refazer = []
while True:
    
    try:
        
        comand = str(input("Digite um comando (listar, desfazer, refazer ou limpar) ou uma tarefa: "))
        comand = comand.lower()
        print()

        
        """
        if comand == 'exit':
            break

        elif comand == 'listar':

            if len(tarefas)==0:
                print("Não há tarefas\n")
            else:
                print("TAREFAS")
                for t in tarefas:
                    print(f'\t-{t}')

        elif comand == 'desfazer':
            if not tarefas:
                print("Nao há tarefas para desfazer")
            refazer.append(tarefas.pop())

            print("TAREFAS")
            for t in tarefas:
                print(f'\t-{t}')

        elif comand == 'refazer':
            if not refazer:
                print("nao ha tarefas para refazer")
            tarefas.append(refazer.pop())

            print("TAREFAS")
            for t in tarefas:
                print(f'\t-{t}')

        elif comand == 'limpar':
            print("Lista de tarefas limpa")
            tarefas = []

        elif comand == 'clear':
            print("\n" * os.get_terminal_size().lines)

        else:
            print(f'"{comand}" adicionado à lista de tarefas')
            tarefas.append(comand)
        """

#Podemos escrever uma nova solucao sem a utilizacao de tantos condicionais:

        if comand == 'exit':
            break

        comandos = {
            'listar': lambda: listar(tarefas),
            'desfazer': lambda: desfazer(tarefas, refazer),
            'refazer': lambda: refazer_tarefas(tarefas, refazer),
            'limpar': lambda: limpar(tarefas),
            'clear': lambda: limpar_console(),
            'adicionar': lambda: adicionar(comand, tarefas)
        }

        comando = comandos.get(comand) if comandos.get(comand) is not None else \
            comandos['adicionar']

        comando()

        salvar(tarefas, CAMINHO_ARQUIVO)

    except:
        print("ERRO")