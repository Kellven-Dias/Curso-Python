
class Multiplicar:

    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):

        def intern(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiplicador
        
        return intern
    
class SomarUm:
    
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        result = self._func(*args, **kwargs)
        return result + 1

@Multiplicar(10)
def soma(x, y):
    return x + y

@SomarUm
def mult(x, y):
    return x * y

if __name__ == "__main__":
    
    print(soma(2, 3))
    print(mult(2, 3))