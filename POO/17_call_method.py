#Ao definirmos o método __call__ em uma classe, a instância dessa classe se torna um objeto "callable"

class Phone:
    def __init__(self, number:str):
        self.number = number

    def __call__(self):
        return print(f'Ligando para {self.number}...')
    
if __name__ == "__main__":
    phone = Phone('(67)99239-1234')
    phone() #Ligando para (67)99239-1234...