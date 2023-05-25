'''
    Simulador de algoritmos de processos utilizando threads
'''
import threading
import time
import random
import operator

class Processo:

    def __init__(self, id, chegada, cpu):
        self.id = id
        self.chegada = chegada
        self.cpu = cpu

    def get_cpu(self):
        return self.cpu

    def get_chegada(self):
        return self.chegada

    def get_id(self):
        return self.id

class FilaAptos:
    listaProcessos = []

    def __init__(self):
        pass

    def insere_processo(self, processo):
        self.listaProcessos.append(processo)

    def mostra_dados_processo(self, posicao):
        print(f'Identificação......: {self.listaProcessos[posicao].get_id()}')
        print(
            f'Chegada............: {self.listaProcessos[posicao].get_chegada()}'
        )
        print(f'CPU................: {self.listaProcessos[posicao].get_cpu()}')

    def get_proximo_processo(self):
        return self.listaProcessos.pop(0)

    def mostra_processos_lista(self):
        for i in range(len(self.listaProcessos)):
            self.mostra_dados_processo(i)

    def tamanho_lista(self):
        return len(self.listaProcessos)

    def ordenarProcesso(self):
        self.listaProcessos.sort(key=operator.attrgetter('cpu'))


class ThreadFCFS(threading.Thread):
    tempo_relogio = 0
    media = 0.0

    def __init__(self, fila_aptos):
        self.fila_aptos = fila_aptos
        threading.Thread.__init__(self)

    def escalonar(self):
        self.fila_aptos.ordenarProcesso()
        qtd = self.fila_aptos.tamanho_lista()
        for i in range(self.fila_aptos.tamanho_lista()):
            proc = self.fila_aptos.get_proximo_processo()
            self.tempo_relogio += proc.get_cpu()

        return (self.tempo_relogio - proc.get_cpu()) / qtd  # media

    def run(self):
        print('Algoritmo FCFS')
        print(f'Media de espera: {self.escalonar()}')


def main():
    p1 = Processo(1, 0, 23)
    p2 = Processo(2, 0, 3)
    p3 = Processo(3, 0, 3)

    f_aptos = FilaAptos()
    f_aptos.insere_processo(p1)
    f_aptos.insere_processo(p2)
    f_aptos.insere_processo(p3)

    f_aptos.mostra_processos_lista()

    fcfs = ThreadFCFS(f_aptos)
    fcfs.start()
    fcfs.join()


main()
