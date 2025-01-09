import json
#somente dados simples


pessoa = {
    'nome': 'Kellven',
    'sobrenome': 'Dias',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open("Intermediário\\21_salvar_dados.json", 'w', encoding='utf8') as arquivo:
    json.dump(pessoa,
               arquivo,
               ensure_ascii=False,
               indent=2)
    
with open("Intermediário\\21_salvar_dados.json", 'r', encoding='utf8') as arquivo:
    pessoa_importa = json.load(arquivo)
    print(pessoa_importa, type(pessoa_importa), sep='\n')
