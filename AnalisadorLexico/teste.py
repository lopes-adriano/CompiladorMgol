import numpy as np
from classToken import Token


#x =Token("classe", "lexema", "tipo")
#print(x)

def teste():
    with open("testeFile.txt", "r") as f:
        for c in f:
            if c.strip():
                print(c)

teste()