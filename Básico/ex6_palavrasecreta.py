import os


secret_word = 'HAPPY'
acertos = ''
contador = 0

while True:

    

    tentativa = input('Digite uma letra: ')
    tentativa = tentativa.upper()
    contador+=1

    if len(tentativa) > 1:
        print('Digite apenas uma letra')
        continue

    if tentativa in secret_word:
        acertos += tentativa

    word = ''
    for letter in secret_word:

        if letter in acertos:
            word += letter
            
        else:
            word+='*'
            

    print(word)
    if(word == secret_word):
        os.system('cls')
        print(f'Parabéns voce acertou a palavra {word} com {contador} tentativas')
        acertos = ''
        contador = 0
        



