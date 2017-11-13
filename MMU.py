class Memory:
    cont = 0

    '''TRUE => espaco livre'''
    def __init__(self, status, base, space):
        self.status = status
        self.base = base
        self.space = space
        self.id = Memory.cont
        Memory.cont += 1

def lista_processos (memory):
    aux = Memory(True, 0, memory)
    return [aux]

def best_fit (lista, size):
    aux = Memory(False, 0, 0) # dummy
    for mem in lista:
        if not mem.status: '''espaco ocupado'''
            continue
        else:
            if mem.space >= size:
                if not aux.status:
                    aux = mem
                else:
                    if aux.space > mem.space:
                        aux = mem
                    else:
                        continue
        return aux


def worst_fit(lista, size):
    aux = Memory(False, 0, 0)  # dummy
    for mem in lista:
        if not mem.status: '''espaco ocupado'''
            continue
        else:
            if mem.space >= size:  '''processo cabe na memoria'''
                if not aux.status:  '''nenhum espaco'''
                    aux = mem
                else
                    if aux.space < mem.space:
                        aux = mem
                    else:
                        continue
    return aux

