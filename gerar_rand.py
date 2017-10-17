import sys
import random

TOTAL_MAX = int(sys.argv[1])
VIRTUAL_MAX  = int(sys.argv[2])
S  = int(sys.argv[3])
P = int(sys.argv[4])

# RAND
total = random.randint(TOTAL_MAX * 0.1, TOTAL_MAX)
virtual  = random.randint(VIRTUAL_MAX * 0.1, VIRTUAL_MAX)
s = random.randint(S * 0.1, S)
p = random.randint(P * 0.1, P)



