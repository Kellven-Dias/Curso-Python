from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    #metodo abstrato: Devem ser implementados nas subclasses
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    #metodos concretos
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')
    
class LogFileMixin(Log):#aqui que deve ser implementada as funcionalidades
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

        print(msg)

class LogPrintMixin(Log):#aqui que deve ser implementada as funcionalidades
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('log error')
    lp.log_success('log success')

    lf = LogFileMixin()
    lf.log_error('log error')
    lf.log_success('log success')
    print(LOG_FILE)