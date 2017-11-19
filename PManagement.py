from Proc import *
from Pages import *
from Events import *

def optimal ():
    pass

def fifo ():
    pass

def LRU2 ():
    pass

def LRU4 ():
    pass

def access (event):
    page = None
    pos = event.acc.space
    for p in event.proc.pp:
        if pos >= p.beg and pos <= pos:
            page = p
            break
    # check if it is on physical memory
    if event.physical is None:
        print('n tah na memoria fisica')
    else:
        print("\tAccessing space " + event.acc.space + " on process " + event.acc.proc.nome)