import numpy as np
from classToken import Token


#x =Token("classe", "lexema", "tipo")
#print(x)

def teste():
    with open("FONTE.alg", "r") as f:
        tamanhoAntes = len(f.read())
        f.seek(0)
        f.seek(45)
        b = f.read()
        f.seek(0)
        f.seek(45)
        tamanhoDepois = len(f.read())
        print(b)
        print(tamanhoAntes)
        print(tamanhoDepois)

#teste()

def what():
    with open("FONTE.alg", "r") as f:
        tamanho = len(f.read())
        f.seek(0)
        for x in range(tamanho):
            c = f.read(1)
            if(c == "\n"):
                print(f"___   \\n   ___")
            elif(c == " "):
                print(f"___   Espaço   ___")
            elif(c == "\t"):
                print(f"___   \\t   ___")
            else:
                print(f"___   {c}   ___")

def what2():
    with open("FONTE.alg", "r") as f:
        arquivo = f.read()
        for c in arquivo:
            if(c == "\n"):
                print(f"___   \\n   ___")
            elif(c == " "):
                print(f"___   Espaço   ___")
            elif(c == "\t"):
                print(f"___   \\t   ___")
            else:
                print(f"___   {c}   ___")



def what3():
    with open("FONTE.alg", "r") as f:
        tamanho = len(f.read())
        f.seek(0)
        c = f.read(tamanho)
        print(c)


what3()