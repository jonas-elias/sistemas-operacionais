import threading
import time

def thread_n_vezes():
    n_vezes = 10
    sem = threading.Semaphore(n_vezes)

    for i in range(11):
        sem.acquire()
        print(f'Executando {i+1} vezes')


threading.Thread(target=thread_n_vezes).start()