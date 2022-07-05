import os

with open('demofile.txt', 'r') as f:
    print(f.read())
    print(f.tell())
    print(f.seek(1))
    print(f.tell())
    print(f.read())
    print(f.seek(2))
    print(f.read())
