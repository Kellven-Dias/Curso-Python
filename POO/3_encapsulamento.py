#Python n possui modificadores de acesso
#São usadas convenções para isto
# sem underline = public
# 1 underline = protected
# 2 underline = private

class Exemplo:

    def __init__(self):
        self.public = 'publico'
        self._protected = 'protected'
        self.__private = 'private'

    def public_method(self):
        print(self.__private)
        self.__private_method()
        return 'public method'
    
    def _proteced_method(self):
        return print('_protected_method')
    
    def __private_method(self):
        return print('private_method')