import os, random

class Numeros():

    listagem = []
    quantidade = 0

    def __init__(self, quantidade):
        self.quantidade = quantidade

    def preencherListagem(self):
        for i in range(self.quantidade):
            self.listagem.append(random.randint(0, 999))

    def mostrarListagem(self):
        print(self.listagem)

    def numeros(self, par):
        print(f"PID {os.getpid()}")
        if par:
            print("Filho dos pares")
            for i in range(len(self.listagem)):
                if self.listagem[i] % 2 == 0:
                    print(self.listagem[i])   
        else:
            print("Filho dos ímpares")
            for i in range(len(self.listagem)):
                if self.listagem[i] % 2 != 0:
                    print(self.listagem[i])

def main():
    numeros = Numeros(10)
    numeros.preencherListagem()
    numeros.mostrarListagem()
    filho1 = os.fork()
    if (filho1 == 0):
        filho1_1 = os.fork()
        if (filho1_1 == 0):
            lista = numeros.listagem
            lista.sort(reverse=True)
            numeros.listagem = lista
            numeros.numeros(True)
    else:
        os.wait()
        filho2 = os.fork()
        if (filho2 == 0):
            filho2_1 = os.fork()
            if (filho2_1 == 0):
                lista = numeros.listagem
                lista.sort(reverse=True)
                numeros.listagem = lista
                numeros.numeros(False)

main()
