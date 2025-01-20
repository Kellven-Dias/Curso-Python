from abc import ABC, abstractmethod #ABCMeta

class Log(ABC): #ou class Log(metaclass = ABCMeta)

    #metodo abstrato: Devem ser implementados nas subclasses
    @abstractmethod #ou seja, a classe Log n pode ser usada diretamente
    def _log(self, msg):...
    
    #metodos concretos
    def log_error(self, msg):
        self._log(f'Error: {msg}')
 
    def log_success(self, msg):
        self._log(f'Success: {msg}')

#como essa classe é herdeira de Log, ela deve implementar o metodo abstrato
#TODAS as classes filhas de uma classe abstrata devem implementar o metodo abstrato
class LogPrintMixin(Log):#aqui que deve ser implementada as funcionalidades
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

#l = Log() gera um TypeError