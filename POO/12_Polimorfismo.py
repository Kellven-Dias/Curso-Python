#Polimorfismo permite que subclasses tenham metodos iguais (mesma assinatura)
#mas com comportamentos diferentes
#Assinatura do método = mesmo nome e qntd de parâmetros.
#Principio da substituição de Liskov:
#Objetos de uma superclasse devem ser substituíveis por objetos de subclasses
#sem que haja uma quebra da aplicação
from abc import abstractmethod, ABC

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def enviar(self)-> bool:...

class NotificacaoEmail(Notificacao):

    def enviar(self)->bool:
        print("Enviando email: ", self.msg)
        return True
    
class NotificacaoSMS(Notificacao):

    def enviar(self)->bool:
        print("Enviando SMS: ", self.msg)
        return True
    
#principio da substituicao de Liskov
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificacao enviada!")
    else:
        print("Notificacao NAO enviada!")


notificacao_email = NotificacaoEmail("Olá email")
notificacao_sms = NotificacaoSMS("Ola sms")

notificar(notificacao_email)
notificar(notificacao_sms)

