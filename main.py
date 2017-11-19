import re
import sys
from Proc import *
# from MMU import *
from Utils import *
from Events import *

def running (entry, mmu, pages, tempo = sys.maxsize):
    # READING ENTRY FILE
    with open(entry) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    # tamanho das memorias fisica e virtual
    size = [0, 0]
    agenda_louca = []
    # fim do programa
    fim = 0
    #lista de espacos requeridos para o quick fit
    spaces = []
    #lista de acessos
    list_acc = []
    mmu_option = int(mmu)
    page_option = int(pages)

    # PROCESSSA O ARQUIVO DE ENTRADA
    for c in content:
        aux = re.sub("\s\s+", " ", c)
        aux = aux.split(" ")

        if len(aux) == 4:
            size[0] = int(aux[0])
            size[1] = int(aux[1])
            unit_aloc = int(aux[2])
            size_page = int(aux[3])
            mem_fisica = physical_memory(size[0], size_page)
            mem_virtual = virtual_memory(size[1])
        elif len(aux) == 2:
            # DEVEMOS COMPACTAR
            agenda_louca.append(Events(Events.COMPACT, aux[0], None, None))
            if fim < int(aux[0]):
                fim = int(aux[0])
        else:
            aux = Process(aux[3], aux[0], aux[1], aux[2], aux[4:])
            aux.real_space(unit_aloc)
            aux.get_pages(size_page)
            aux.translate()
            if aux.mem in spaces:
                continue
            else:
                spaces.append(aux.mem)
            for ev in aux.acc:
                agenda_louca.append(ev)
            agenda_louca.append(Events(Events.INSERT, aux.ti, aux))
            agenda_louca.append(Events(Events.DELETE, aux.tf, aux))
            if aux.tf > fim:
                fim = aux.tf

    agenda_oficial = []
    for m in range(fim):
        agenda_oficial.append([])

    for event in agenda_louca:
        agenda_oficial[event.moment-1].append(event)
        if event.kind == Events.ACCESS:
            list_acc.append(event.acc)
    elapsed_time = 0

    for a in agenda_oficial:
        a.sort()
        
    list_acc.sort()

    while elapsed_time < fim:
        print("Instante " + str(elapsed_time + 1))
        for e in agenda_oficial[elapsed_time]:
            make_it_happen(e, [mmu_option, page_option], [mem_fisica, mem_virtual], size[1], list_acc, spaces)
        if (elapsed_time + 1) % tempo == 0:
            status(mem_fisica, mem_virtual)
        elapsed_time += 1
    #status(mem_fisica, mem_virtual)

def console ():
    working = True
    var = 0
    entries = [[False, ""], [False, 0], [False, 0]]
    while working:
        cmd = input("[ep3]: ")
        
        if cmd == 'sai':
            working = False
        elif cmd[0:7] == 'carrega':
            entries[0][1] = cmd.split(" ")[1]
            if not entries[0][0]:
                entries[0][0] = True
                var += 1
        elif cmd[0:6] == "espaco":
            entries[1][1] = cmd.split(" ")[1]
            if not entries[1][0]:
                entries[1][0] = True
                var += 1
        elif cmd[0:9] == "substitui":
            entries[2][1] = cmd.split(" ")[1]
            if not entries[2][0]:
                entries[2][0] = True
                var += 1
        elif cmd[0:7] == "executa":
            #timing = cmd.split(" ")[1]
            if var == 3:
                running(entries[0][1], entries[1][1], entries[2][1])
                entries = [[False, ""], [False, 0], [False, 0]]
            else:
                continue
        else:
            print("Invalid option")
            continue

def status (p_mem, v_mem):
    for v in v_mem:
        print(v)
    print('')
    for p in p_mem:
        print(p)
    print('')

if len(sys.argv) == 1:
    console()
else:
    running(sys.argv[1], sys.argv[2], sys.argv[3], 2)

