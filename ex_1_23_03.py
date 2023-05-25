import os

def pai(id):
    print(f"Eu sou o processo {os.getpid()} pai de {id}")

def filho():
    print(f"Eu sou o processo {os.getpid()} filho de {os.getppid()}")

def main():
    id = os.fork()
    if (id == 0):
        filho()
    else:
        pai(id)
main()