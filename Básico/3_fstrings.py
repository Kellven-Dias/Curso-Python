nome = 'Kellven Dias'
peso = 75.0
altura = 1.73

imc = peso / altura**2

print(nome, 'possui peso =', peso, 'e altura =', altura, 'e seu IMC é igual a', imc)

##formatação de strings

linha = f'{nome} tem {altura:.2f} de altura e pesa {peso:.1f} kg e seu IMC é igual a {imc:.2f}'
print(linha)

#format
a='Kellven'
b='Dias'
c=1.564324


string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)

string = 'a={2} b={0} c={1}'
formato = string.format(a, b, c)
print(formato)

#(Caractere)(><^)(quantidade)
# (=): forca aparecer sinal antes do numero
palavra = 'KELL'
print(f'{palavra: >10}') #L
print(f'{palavra:-<10}') #R
print(f'{palavra:_^10}') #C
print(f'{3.14159265358979:0=+10.2f}')
print(f'o hexadecimal de 100 é {100:04X}')



