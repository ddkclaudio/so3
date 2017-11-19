from Proc import *
from Pages import *
from Events import *

def optimal ():
    pass

def fifo (event, p_mem, list_acc):
    aux = list_acc.pop(0)
    new_proc_page = event.acc.page
    v_page = aux.page
    p_page = v_page.physical
    p_page.virtual = new_proc_page
    v_page.physical = None

def LRU2 ():
    pass

def LRU4 ():
    pass

def access (event, p_mem, list_acc, opt):
    page = None
    pos = event.acc.space
    for p in event.proc.pp:
        if pos >= p.beg and pos <= pos:
            page = p
            break
    # check if it is on physical memory
    if event.acc.page.physical is None:
        quadro = search_page(p_mem)
        if quadro.beg == quadro.end:
            #n tem memoria
            print('sub page')
            access(event, p_mem, list_acc, opt)
        else:
            # print(quadro)
            quadro.virtual = event.acc.page
            # if event.acc.page is None:
                # print('FUDEU !!!!!!!')
            # print(quadro)
            event.acc.page.physical = quadro
            print("\tAccessing space " + str(event.acc.space) + " on process " + event.acc.proc.nome)
    else:
        print("\tAccessing space " + str(event.acc.space) + " on process " + event.acc.proc.nome)
        
def search_page (memoria):
    aux = P_pages(0,0)
    for mm in memoria:
        if mm.is_free():
            aux = mm
            break
    return aux
    
def sub_page (event, p_mem, list_acc, opt):
    if opt == 1:
        optimal()
    elif opt == 2:
        fifo(event, p_mem, list_acc)
    elif opt == 3:
        LRU2()
    elif opt == 4:
        LRU4()
    else:
        print('Error-> sub_page: Invalid option')
    
