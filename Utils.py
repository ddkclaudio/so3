from MMU import *

# Base para Best/Worst Fit
def lista_processos (qtd_memory):
    aux = Memory(0, qtd_memory)
    return [aux]

def best_fit(lista, procc):
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
# @recebe uma lista com os tamanhos e a lista com as memorias
# @devolve uma lista de listas com todos os espacos disponiveis
def get_spaces(list, tamanhos):
    print("get\_spaces: running")
    free = []
    for t in tamanhos:
        aux = []
        for cell in list:
            base = cell.base
            maximo = base + cell.space
            while base + t < maximo:
                aux1 = Memory(base, t)
                aux.append(aux1)
                base += t
        aux.sort()
        free.append(aux)
    print("get\_spaces: ended")
    return free


# param --- the process to be allocated
# devolve um
def quick_fit(procc, ua, proc_list):
    aux = Memory(0, 0)
    i = 0
    for l in proc_list:
        if l != []:
            if l[0].mem == procc.mem:
                aux = l[0]
                l.remove(aux)
    # on this point, user knows in that list to pick the
    # first avaible memory from
    return aux


# n estamos levando em conta a possubilidade de dar ruim na escolha de onde por os processos
def into_memory (procc, option, list_memory):
    if option == Memory.BEST:
        best_local  = best_fit(list_memory, procc)
        if best_local.space == 0:
            print("Error: process can\'t be placed in virtual memory")
        else:
            index = list_memory.index(best_local)
            if procc.mem < list_memory[index].space:
                list_memory.insert(index, Memory(0, procc.mem, procc))
                list_memory[index + 1].base += procc.mem
                list_memory[index + 1].space -= procc.mem
            else:
                list_memory[index].pr += procc
    elif option == Memory.WORST:
        best_local  = worst_fit(list_memory, procc)
        if best_local.space == 0:
            print("Error: process can\'t be placed in virtual memory")
        else:
            index = list_memory.index(best_local)
            if procc.mem < list_memory[index].space:
                list_memory.insert(index, Memory(0, procc.mem, procc))
                list_memory[index + 1].base += procc.mem
                list_memory[index + 1].space -= procc.mem
            else:
                list_memory[index].pr += procc
    elif option == Memory.QUICK:
        # inserting an occupied memory into list_memory
        pass
    else:
        print("Error: into_memory invalid option")

def out_of_memory (proc):
    pass

# Inserir
# [   [free, 0, 32]   ]

# [  [proc0, 0, 8], [free, 0, 32] ]

# [  [proc0, 0, 8], [free, 8, 24] ]

# Remover
# [ [free, 0, 18], [proc1, 18, 6], [proc2, 24, 8] ]

# [ [free, 0, 18], [free, 18, 6], [proc2, 24, 8] ]

# [ [free, 0, 24], [proc2, 24, 8] ]