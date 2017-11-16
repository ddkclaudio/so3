class Process:
    count = 0

    def __init__(self, nome, ti, tf, mem, acc):
        self.id = Process.count
        Process.count += 1
        self.nome = nome
        self.ti = int(ti)
        self.tf = int(tf)
        self.mem = int(mem)
        self.acc = acc #lista de acessos

    def __lt__(self, other):
        return self.ti < other.ti