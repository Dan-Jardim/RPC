import rpyc
import time

class MyService(rpyc.Service):
    
    def __init__(self):
        super().__init__()
        self.start = 0
        self.end = 0
    
    # código que é executado quando uma conexão é iniciada, caso seja necessário
    def on_connect(self, conn):
        self.start = time.time()

        pass

    # código que é executado quando uma conexão é finalizada, caso seja necessário
    def on_disconnect(self, conn):
        self.end = time.time()

        print(f"Execution time: {self.end - self.start} s.")

        pass

    # este é um método exposto
    def exposed_get_answer(self):
        return 42

    # este é um atributo exposto
    exposed_the_real_answer_though = 43

    # este método não é exposto
    def get_question(self): 
        return "Qual é a cor do cavalo branco de Napoleão?"

#Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
  
    t = ThreadedServer(MyService, port=18861)
  
    t.start()
