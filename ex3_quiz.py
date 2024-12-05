
perguntas = [
    {
        'pergunta': 'Quanto é 2x2?',
        'alternativas': ['1','3', '4', '5'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5x5?',
        'alternativas': ['1','10','25','36'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'alternativas': ['2', '5', '6', '12'],
        'resposta': '5',
    },
]


count = 0
for i in perguntas:
    print('Pergunta:', i['pergunta'])

    print('Alternativas:')
    for j in range(len(i['alternativas'])):
        print(f'{j})', i['alternativas'][j])

    result = input('Escolha uma opção: ')

    if result == i['resposta']:
        count+=1
        print("Resposta correta!\n")
    else:
        print('Resposta errada\n')

print(f'Você acertou {count} de {len(perguntas)} perguntas!!')

#outra solução

i = 0
qtd_acertos = 0
for p in perguntas:
    print("Pergunta:", p['pergunta'])

    opcoes = p['alternativas']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)

    escolha = input("Escolha uma opcao: ")

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == p['resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Acertou')
    else:
        print('Errou')

    print(f'voce acertou {qtd_acertos} de {len(perguntas)}')
