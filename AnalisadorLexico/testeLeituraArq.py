import os



with open('testeFile.txt', 'r') as f:
    for i in range(50):
        h = f.read(1)
        print(h)