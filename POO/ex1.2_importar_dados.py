from ex1_1_salvar_dados import Pessoa, dump_json

import json

with open("POO\\ex1_1_dados.json", 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)


p1 = Pessoa(**pessoas[0])
p2 = Pessoa(**pessoas[1])

print(p1.__dict__, p2.__dict__, sep='\n')

