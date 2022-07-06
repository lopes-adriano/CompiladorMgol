import numpy as np
from classToken import Token


#x =Token("classe", "lexema", "tipo")
#print(x)

varGlobal = 0

def ts():
    global varGlobal
    for r in range(10):
        print(r)
        varGlobal += r


ts()
print(varGlobal)