import sys
from MMU import *
from Utils import *

with open(sys.argv[1]) as f:
    content = f.readlines()
content = [x.strip() for x in content]

