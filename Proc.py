class Process:
    identifier = 0

    def __init__(self, nome, ti, tf, mem, acc):
        self.id = Process.identifier
        Process.identifier += 1
        self.nome = nome
        self.ti = ti
        self.tf = tf
        self.mem = mem
        self.acc = acc #lista de acessos

