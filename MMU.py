import Proc

class Memory:
    cont = 0

    '''TRUE => espaco livre'''
    def __init__(self, base, space, pr = None):
        self.base = base
        self.space = space
        self.process = pr
        self.id = Memory.cont
        Memory.cont += 1
