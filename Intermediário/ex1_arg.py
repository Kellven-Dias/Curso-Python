def mult(*args):
    mult=1
    for num in args:
        mult *= num
    return mult

print(mult(2,2,2))

def par_impar(num):
    return print(f'{num} é par') if num%2==0 else print(f'{num} é impar')

par_impar(2)
par_impar(3)
    
