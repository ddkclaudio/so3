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
            if not cell.process:
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


# param --- the process to be allocated and the
# devolve um
def quick_fit(mem_list, procc):
    aux = Memory(0, 0)
    i = 0
    for ll in mem_list:
        if not ll == []:
            if ll[0].mem >= procc.mem:
                aux = ll[0]
    # on this point, user knows in that list to pick the
    # first available memory from
    return aux


# params    ==> the process, the option, the virtual memory, and the list of spaces to be required
# it does   ==> try to place the process on the virtual memory
def into_memory (procc, option, list_memory, spaces_list):
    if option == Memory.BEST:
        best_local  = best_fit(list_memory, procc)
        if best_local.space == 0:
            print("Error: process can\'t be placed in virtual memory")
        else:
            index = list_memory.index(best_local)
            if procc.mem < list_memory[index].space:
                list_memory.insert(index, Memory(best_local.base, procc.mem, procc))
                list_memory[index + 1].base += procc.mem
                list_memory[index + 1].space -= procc.mem
            else:
                list_memory[index].pr = procc
    elif option == Memory.WORST:
        best_local  = worst_fit(list_memory, procc)
        if best_local.space == 0:
            print("Error: process can\'t be placed in virtual memory")
        else:
            index = list_memory.index(best_local)
            if procc.mem < list_memory[index].space:
                list_memory.insert(index, Memory(best_local.base, procc.mem, procc))
                list_memory[index + 1].base += procc.mem
                list_memory[index + 1].space -= procc.mem
            else:
                list_memory[index].pr = procc
    elif option == Memory.QUICK:
        # inserting an occupied memory into list_memory
        best_local  = quick_fit(get_spaces(list_memory, spaces_list), procc)
        if best_local.space == 0:
            print("Error: process can\'t be placed in virtual memory")
        else:
            # step 1 -- where to put it
            index = 0
            done = False
            while list_memory[index + 1] != None and not done:
                if list_memory[index].process:
                    continue
                elif list_memory[index].base == best_local.base:
                    list_memory.insert(index, Memory(best_local.base, procc.mem, procc))
                    list_memory[index + 1].base += procc.mem
                    list_memory[index + 1].space -= procc.mem
                    done = True
                elif list_memory[index + 1] > best_local.base:
                    done = True
                    list_memory[index].space = best_local.base - list_memory[index].base
                    list_memory.insert(index + 1, best_local)
                    a_base = list_memory[index+1].base + list_memory[index + 1].space
                    a_space = list_memory[index + 2] - a_base
                    list_memory.insert(index + 2, Memory(a_base, a_space))
            # staring at the last part of memory
            if list_memory[index].base == best_local.base and not done:
                if procc.mem < list_memory[index].space:
                    list_memory.insert(index, Memory(best_local.base, procc.mem, procc))
                    list_memory[index + 1].base += procc.mem
                    list_memory[index + 1].space -= procc.mem
                else:
                    list_memory[index].pr = procc
            elif list_memory[index].base < best_local.base and not done:
                list_memory[index].space = best_local.base - list_memory[index].base
                list_memory.append(best_local)

    else:
        print("Error -- into_memory: invalid option")

def out_of_memory (proc,m_list):
    i = 0
    found = False
    while m_list[i] and not found:
        if m_list[i].process and m_list[i].process == proc:
            found = True
            m_list[i].process = None
            if m_list[i + 1] and not m_list[i + 1].process:
                m_list[i].space += m_list[i + 1].spaces
                m_list.pop(i+1)
            if m_list[i - 1] and not m_list[i - 1].process:
                m_list[i - 1].space += m_list[i].spaces
                m_list.pop(i)
        i += 1

# Inserir
# [   [free, 0, 32]   ]

# [  [proc0, 0, 8], [free, 0, 32] ]

# [  [proc0, 0, 8], [free, 8, 24] ]

# Remover
# [ [free, 0, 18], [proc1, 18, 6], [proc2, 24, 8] ]

# [ [free, 0, 18], [free, 18, 6], [proc2, 24, 8] ]

# [ [free, 0, 24], [proc2, 24, 8] ]

# Exemplo3 (colocar um processo de 6 bits no espaco 19 -- n sei se isso aconteceria)

# [ [proc0, 0, 7], [free, 7, 5], [proc1, 12, 6], [free, 18, 8], (place it here) [proc2, 26, 6] ]

# [ [proc0, 0, 7], [free, 7, 5], [proc1, 12, 6], [free, 18, 8], [proc3, 19, 6], [proc2, 26, 6] ]
#                                                   [index]      [index + 1]
# [ [proc0, 0, 7], [free, 7, 5], [proc1, 12, 6], [free, 18, 1], [proc3, 19, 6], [free, 25, 1], [proc2, 26, 6] ]
