'''
    Considere um programa multithread onde o usuário irá determinar a quantidade de threads
    e a quantidade de vezes que cada uma das thread irá executar. Escreva um programa
    em Python para resolver este problema
'''
import time
import threading as th


class Program(th.Thread):
    thread = 0
    qtd_execucoes = 0

    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        for i in range(self.qtd_execucoes):
            print(f'Thread número {self.thread}')
            time.sleep(1)


def main():
    threads = int(input('Número de threads: '))

    programs = []
    for i in range(threads):
        qtd = int(
            input(
                f'Número de vezes que a thread de número {i} irá executar: '))
        program = Program()
        program.thread = i
        program.qtd_execucoes = qtd
        programs.append(program)

    for i in range(threads):
        programs[i].start()


main()
