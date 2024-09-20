#str.strip() -> remove os espaços antes e depois da frase
#str.split() -> separa a str em uma lista, para cada obj separado por espaço
#str.split(',') -> separa a str em uma lista, para cada obj separado por ','

phrase = 'O rato roeu a roupa do Rei de Roma'

print(phrase.split())

phrase = 'O rato, roeu a roupa, do rei de roma'

print(phrase.split(','))

phrase = '                     O rato roeu a roupa do Rei de Roma                     '
print(phrase.strip())

phrase = '    o rato roeu   , a roupa do rei de roma     '
phrase = phrase.split(',')
new_phrase = []

for i, phrases in enumerate(phrase):
    new_phrase.append(phrase[i].strip())

print(new_phrase)

joined_phrases = '_'.join(new_phrase)
print(joined_phrases)

phrase = '07808525162'
joined_phrases = '.'.join(phrase)
print(joined_phrases)
