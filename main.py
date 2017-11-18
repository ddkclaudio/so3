import sys
import re
from MMU import *
from Proc import *
from Utils import *
from Events import *

def running (entrada, mmu, pages):
    # LE O ARQUIVO DE ENTRADA
    with open(entrada) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    # tamanho das memorias fisica e virtual
    size = [0, 0]
    agenda_louca = []
    # fim do programa
    fim = 0
    #lista de espacos requeridos para o quick fit
    spaces = []
    mmu_option = int(mmu)
    page_option = int(pages)

    # PROCESSSA O ARQUIVO DE ENTRADA
    for c in content:
        aux = re.sub("\s\s+", " ", c)
        aux = aux.split(" ")

        if len(aux) == 4:
            size[0] = int(aux[0])
            size[1] = int(aux[1])
            mem_fisic = lista_processos(size[0])
            mem_virtual = lista_processos(size[1])
            unit_aloc = aux[2]
            size_page = aux[3]
        elif len(aux) == 2:
            # DEVEMOS COMPACTAR
            agenda_louca.append(Events(Events.COMPACT, aux[0], None, None))
            if fim < int(aux[0]):
                fim = int(aux[0])
        else:
            aux = Process(aux[3], aux[0], aux[1], aux[2], aux[4:])
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
    elapsed_time = 0

    for a in agenda_oficial:
        a.sort()

    while elapsed_time < fim:
        print("Instante " + str(elapsed_time + 1))
        for e in agenda_oficial[elapsed_time]:
            make_it_happen(e, [mmu_option, page_option], mem_virtual, size[1], spaces)
        elapsed_time += 1

def console ():
    working = True
    var = 0
    entries = [[False, ""], [False, 0], [False, 0]]
    while working:
        cmd = input("[ep3]: ")
        if cmd == "sai":
            working = False
        elif cmd[0:7] == 'cwarrega':
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
            #entries[2][1] = cmd.split(" ")[1]
            if var == 3:
                running(entries[0][1], entries[1][1], entries[2][1])
                entries = [[False, ""], [False, 0], [False, 0]]
            else:
                continue
        else:
            print("Invalid option")
            continue


if len(sys.argv) == 1:
    console()
else:
    running(sys.argv[1], sys.argv[2], sys.argv[3])

