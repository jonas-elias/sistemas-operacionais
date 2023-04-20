import time
import threading

class ThreadNumeroParImpar(threading.Thread):   
    def __init__(self, x, method):
        self.x = x
        self.method = method
        threading.Thread.__init__(self)
        
    def run(self):
        if (self.method == 'Par'):
            self.par()
        elif (self.method == 'Impar'):
            self.impar()
    
    def impar(self):
        for i in range(self.x):
            if (i % 2 != 0):
                print(f"Número ímpar {i}")
                time.sleep(0.5)

    def par(self):
        for i in range(self.x):
            if (i % 2 == 0):
                print(f"Número par {i}")
                time.sleep(0.5)

def main():
    ob_par = ThreadNumeroParImpar(10, 'Par')
    ob_impar = ThreadNumeroParImpar(10, 'Impar')
    ob_par.start()
    ob_impar.start()

main()