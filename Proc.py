from Events import *

class Process:
    count = 0

    def __init__(self, nome, ti, tf, mem, acc):
        self.id = Process.count
        Process.count += 1
        self.nome = nome
        self.ti = int(ti)
        self.tf = int(tf)
        self.mem = int(mem)
        self.acc = []
        offset = 0
        size = len(acc)
        while offset < size:
            aux = Events(Events.ACCESS, acc[offset + 1], self, Access(self, acc[offset]))
            self.acc.append(aux)
            offset += 2

    def __lt__(self, other):
        return self.ti < other.ti