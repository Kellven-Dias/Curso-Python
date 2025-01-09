#No windows devemos ter o cuidado de colocar duas barras invertidas para caminhos
# r (leitura), w(escrita), x(criacao)
# a (escreve ao final), b(binario)
# t (modo texto), +(leitura e escrita)

#o 'w' apaga tudo do arquivo e escreve
#o 'a' escreve no final
import os

caminho_arquivo = "C:\\Users\\User\\Documents\\CursoPython\\Intermediário"
caminho_arquivo += "\\20_manipulacao_arquivos.txt"

#arquivo = open(caminho_arquivo, 'r')

#arquivo.close()

#o código acima pode ser reescrito com um context manager:

with open (caminho_arquivo, 'w') as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2")

with open (caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

with open (caminho_arquivo, 'w+') as arquivo:
    arquivo.write("Linha 3\n")
    arquivo.writelines(
        ('Linha 4\n', 'Linha 5\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())

with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write("FIM DA LINHA")

#caso alguns caracteres n funcionem: colocarf ,encoding = 'utf8' no with open

#para remover arquivos ou renomear caminhos ou nomes de arqvs:
#os.remove(caminho_arquivo) #deleta arquivo
#os.unlink(caminho_arquivo) #deleta arquivo
#os.rename(caminho_arquivo, '20_manipula_arquivo.txt')