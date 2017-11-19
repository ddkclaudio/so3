from Proc import *
from Pages import *
from Events import *

def optimal ():
    # formula  'magica'
    aux = list_acc.pop(0)
    new_proc_page = event.acc.page
    v_page = aux.page
    p_page = v_page.physical
    p_page.virtual = new_proc_page
    v_page.physical = None

def fifo (event, p_mem, list_acc):
    aux = list_acc.pop(0)
    new_proc_page = event.acc.page
    v_page = aux.page
    p_page = v_page.physical
    p_page.virtual = new_proc_page
    v_page.physical = None

def LRU2 (event, p_mem):
    i = index_to_kill(len(P_pages.TAB_PAGES[0]))
    new_proc_page = event.acc.page
    p_page = p_mem[i]
    v_page = p_page.virtual
    p_page.virtual = new_proc_page
    v_page.physical = None
    

def LRU4 ():
    # formula  'magica'
    aux = list_acc.pop(0)
    new_proc_page = event.acc.page
    v_page = aux.page
    p_page = v_page.physical
    p_page.virtual = new_proc_page
    v_page.physical = None

def get_matrix (n_pages):
    return [[0 for x in range(n_pages)] for y in range(n_pages)] 
    
def referencia_matriz (n, n_pages):
    aux = P_pages.TAB_PAGES[n]
    for bits in aux:
        bits = 1
    for i in range(n_pages):
        P_pages.TAB_PAGES[i][n] = 0

def index_to_kill (n_pages):
    smaller = sys.maxsize
    index = -1
    for i in range(n_pages):
        soma = 0
        for j in range(n_pages):
            soma += P_pages.TAB_PAGES[i][j]
        if soma < smaller:
            smaller = soma
            index = i
    return index
    

def access (event, p_mem, list_acc, opt):
    # check if it is on physical memory
    if event.acc.page.physical is None:
        # print('Falha de página')
        quadro = search_page(p_mem)
        if quadro.beg == quadro.end:
            #n tem memoria
            sub_page(event, p_mem, list_acc, opt)
            access(event, p_mem, list_acc, opt)
        else:
            # print(quadro)
            quadro.virtual = event.acc.page
            # if event.acc.page is None:
                # print('FUDEU !!!!!!')
            # print(quadro)
            event.acc.page.physical = quadro
            print("\tAccessing space " + str(event.acc.space) + " on process " + event.acc.proc.nome)
    else:
        aux = p_mem.index(event.acc.page.physical)
        referencia_matriz(aux, len(P_pages.TAB_PAGES[0]))
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
        LRU2(event, p_mem)
    elif opt == 4:
        LRU4()
    else:
        print('Error-> sub_page: Invalid option')
    
