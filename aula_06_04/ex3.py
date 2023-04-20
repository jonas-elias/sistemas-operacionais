import threading
import time

class Thread_Exemplo(threading.Thread):
    numero_1 = 0
    numero_2 = 0
    def __init__(self, numero_1, numero_2):
        threading.Thread.__init__(self)
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def run(self):
        print("Thread executando")
        self.subtrair()
        self.somar()

    def subtrair(self):
        print(f"A subtração de {self.numero_1} com {self.numero_2} é {float(self.numero_1 - self.numero_2)}")

    def somar(self):
        print(f"A soma de {self.numero_1} com {self.numero_2} é {float(self.numero_1 + self.numero_2)}")

def main():
    ob = Thread_Exemplo(2, 4)
    ob.start()
    ob.join()
    print("Thread main voltou a executar ...")

main()
