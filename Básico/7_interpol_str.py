#s - string
#d e i - inteiro
#f - float
#x e X - hexadecimal

nome = 'Kellven'
idade = 20
altura = 1.73
var = '%s tem %d anos e mede %.2f' % (nome, idade, altura)
print(var)

var = '%s tem %.4x anos em hexadecimal e mede %.2f' % (nome, idade, altura)
print(var)