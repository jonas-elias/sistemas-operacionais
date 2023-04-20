import threading
import time

class Thread_Exemplo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print(f"Objeto Thread_Exemplo executando {self.id} de 10")
            time.sleep(0.5)

def main():
    obj_th = Thread_Exemplo()
    obj_th.start()
    for i in range(10):
        print(f"Main executando {i} de 10")
        time.sleep(0.5)
    
main()