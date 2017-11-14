from MMU import *

# Base para Best/Worst Fit
def lista_processos (memory):
    aux = Memory(0, memory, -1)
    return [aux]

def best_fit (lista, procc):
    aux = Memory(0, 0)
    for mem in lista:
        # espaco livre
        if mem.process is None and mem.space >= procc.mem:
            if aux.process is None:
                aux = mem
            elif aux.space > mem.space:
                aux = mem
    return aux

def worst_fit(lista, procc):
    aux = Memory(0, 0)  # dummy
    for mem in lista:
        if mem.process is None and mem.space >= procc.mem:
            if aux.process is None:
                aux = mem
            elif aux.space < mem.space:
                aux = mem
    return aux

# Base para Quick Fit
# @recebe a unidade de alocacao e o tamanho da memoria fisica 
# @devolve uma lista de listas com todos os espacos disponiveis    
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

# recebe a lista de listas e o tamanho do processo
# devolve
def quick_fit (lista, procc, ua):
    ind = 0
    while ind*ua < procc.mem:
        ind += 1
    for mm in lista[ind]:
        if mm.process == None:
            mm.process = procc
            break