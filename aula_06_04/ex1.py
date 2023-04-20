import time
import threading

def thread_1():
    for i in range(10):
        print(f"Thread_1 xecução {i} de 10")
        time.sleep(0.5)

def main():
    th_1 = threading.Thread(target=thread_1, name='Thread 1')
    th_1.start()
    for i in range(10):
        print(f"Main - execução {i} de 10")
        time.sleep(0.5)

main()