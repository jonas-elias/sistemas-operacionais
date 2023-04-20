import os

def filho():
    os.execlp("/bin/date", "date")

def main():
    print(f"Eu sou {os.getpid()} ")
    if (os.fork() > 0):
        print(f"Pai {os.getpid()} aguardando...")
        os.wait()
    else:
        print(f"Filho: {os.getpid()}")
        filho()

main()
