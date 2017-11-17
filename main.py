import sys
import re
from MMU import *
from Proc import *
from Utils import *
from Events import *

# LE O ARQUIVO DE ENTRADA
with open(sys.argv[1]) as f:
    content = f.readlines()
content = [x.strip() for x in content]

# tamanho das memorias fisica e virtual
size = [0, 0]
list_proc = []
agenda_louca = []
# fim do programa
fim = 0
mmu_option = int(sys.argv[2])
page_option = int(sys.argv[3])

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
        if fim < aux[0]:
            fim = int(aux[0])
    else:
        aux = Process(aux[3], aux[0], aux[1], aux[2], aux[4:])
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
        make_it_happen(e, [mmu_option, page_option], mem_virtual, size[1])
    elapsed_time += 1
