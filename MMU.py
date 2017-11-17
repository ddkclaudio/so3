import Proc

class Memory:
    count   = 0
    BEST    = 1
    WORST   = 2
    QUICK   = 3

    '''TRUE => espaco livre'''
    def __init__(self, base, space, pr = None):
        self.base       = int(base)
        self.space      = int(space)
        self.process    = pr
        self.id         = Memory.count
        Memory.count    += 1

    def __lt__(self, other):
        return self.base < other.base