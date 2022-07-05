import os

with open("testeFile.txt", "w") as f:
    f.write("O rato roeu a roupa do rei de Roma")

with open('testeFile.txt', 'r') as f:
    for c in f:
        print(c)
    seta = f.tell()
    print(seta)
    f.seek(3)
    print(f.read(36))
    print(f.tell)
