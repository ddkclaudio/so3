import sys
import re
from MMU import *
from Proc import *
from Utils import *

# LE O ARQUIVO DE ENTRADA
with open(sys.argv[1]) as f:
    content = f.readlines()
content = [x.strip() for x in content]

list_proc = []
mmu_option = int(sys.argv[2])

# PROCESSSA O ARQUIVO DE ENTRADA
for c in content:
    aux = re.sub("\s\s+", " ", c)
    aux = aux.split(" ")
    print(aux)

    if len(aux) == 4:
        mem_fisic = lista_processos(aux[0])
        mem_virtual = lista_processos(aux[1])
        unit_aloc = aux[2]
        size_page = aux[3]
    elif len(aux) == 2:
        # DEVEMOS COMPACTAR
        pass
    else:
        list_proc.append(Process(aux[3], aux[0], aux[1], aux[2], aux[4:]))

list_proc.sort()

elapsed_time = 0

while (True):

    for proc in list_proc:
        if proc.ti >= elapsed_time:
            pass

    elapsed_time += 1