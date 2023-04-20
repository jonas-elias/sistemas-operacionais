import time
import threading

class ClasseThread(threading.Thread):
    def __init__(self):
      threading.Thread.__init__(self)
  
    def run(self):
        print(f"Thread com classe {self.name}")
        time.sleep(1)

def Thread_sem_Classe():
    print(f"Thread sem classe {threading.current_thread().name}")
    time.sleep(1)

def main():
    obj = ClasseThread()
    obj.start()
    thread_sem_classe = threading.Thread(target= Thread_sem_Classe, name='th sem classe')
    thread_sem_classe.start()

main()