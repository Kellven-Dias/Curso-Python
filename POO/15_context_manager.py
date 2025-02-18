from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo)
        yield arquivo
    except:
        print("Erro ao abrir arquivo")
    finally:
        print("Fechando arquivo")
        arquivo.close()

with my_open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Teste de escrita')
   
