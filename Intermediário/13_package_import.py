#importação de pacotes(pastas) e módulos(arquivos .py)
from aula_package.modulo import soma #importação da funcao soma do modulo do pacote "aula_package"
import aula_package.modulo as am #importa o modulo inteiro e renomeia para "am" a fim de evitar nomes grandes

print(soma(1, 2))
print(am.subtracao(6, 2))