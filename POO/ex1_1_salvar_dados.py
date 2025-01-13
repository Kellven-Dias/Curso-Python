import json

class Pessoa:

    def __init__(self, nome, sobrenome, idade, profissao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.profissao = profissao
        
p1 = Pessoa('Kellven', 'Dias', 21, 'Engenheiro de Computação')
p2 = Pessoa('Vitória', 'Estevam', 23, 'Nutricionista')
pessoas = [p1.__dict__, p2.__dict__]

def dump_json():
    with open("POO\\ex1_1_dados.json" , 'w', encoding='utf8') as arquivo:
        json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    dump_json()