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

'''
    Base para Best/Worst Fit
'''
def lista_processos (memory):
    aux = Memory(0, memory, -1)
    return [aux]


def best_fit (lista, procc):
    aux = Memory(0, 0) # dummy
    for mem in lista:
        if mem.process == None and mem.space >= procc.mem: '''espaco livre'''
            if aux.process == -1:
                aux = mem
            else:
                if aux.space > mem.space:
                    aux = mem
        return aux


def worst_fit(lista, procc):
    aux = Memory(0, 0)  # dummy
    for mem in lista:
        if mem.process == None and mem.space >= procc.mem: '''espaco livre'''
            if aux.process == -1:
                aux = mem
            else:
                if aux.space < mem.space:
                    aux = mem
        return aux

'''
    Base para Quick Fit
    @recebe a unidade de alocação e o tamanho da memória física 
    @devolve uma lista de listas com todos os espaços disponíveis
'''
def get_spaces (ua, tamanho):
    lista = []
    i = 1
    while i*ua < tamanho:
        aux = []
        size = i*ua
        base = 0
        limit = size
        while limit < tamanho:
            mem = Memory(base, size)
            base += size
            limit += size
            aux += [mem]
        lista += aux
    return lista

'''
    recebe a lista de listas e o tamanho do processo
    devolve
'''
def quick_fit (lista, procc, ua):
    ind = 0
    while ind*ua < procc.mem:
        ind += 1
    for mm in lista[ind]:
        if mm.process == None:
            mm.process = procc
            break

