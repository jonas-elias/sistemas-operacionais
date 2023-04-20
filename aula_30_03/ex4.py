import os

def filho():
    os.execlp("python", "python", "./ex5.py")

def main():
    print(f"Eu sou o programa master. Meu id eh {os.getpid()}")
    if os.fork() > 0:
        print(f"Pai {os.getpid()} aguardando...")
        os.wait()
    else:
        print(f"Filho: {os.getpid()}")
        filho()

main()