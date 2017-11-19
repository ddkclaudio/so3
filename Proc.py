from Events import *
from Pages import *

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
        self.pp = []
        offset = 0
        size = len(acc)
        while offset < size:
            aux = Events(Events.ACCESS, acc[offset + 1], self, Access(self, acc[offset]))
            self.acc.append(aux)
            offset += 2

    def __lt__(self, other):
        return self.ti < other.ti

    # takes the allocation unity
    # returns the real space to be reserved to the space
    def real_space (self, ua):
        aux = int(self.mem/ua)
        if aux*ua == self.mem:
            return  aux
        else:
            return aux + 1


    def get_pages (self, pages):
        b = 0
        e = pages - 1
        while b < self.mem:
            self.pp.append(V_pages(b, e, self))
            b += pages
            e += pages