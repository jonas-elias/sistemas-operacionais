import os

id = os.fork()
if id > 0:
    print(f"Pai executando. Número de identificação {os.getpid()}")
    os.wait()
    print("Pai encerrando a execução")
elif id == 0:
    os.execlp("python3", "python3", "./ex2.py")
else:
    print("Erro no processo")