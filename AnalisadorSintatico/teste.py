import copy
import pandas as pd

actions = pd.read_csv('Actions.csv')
goto = pd.read_csv('goto.csv')


with open('gramatica-Mgol.txt') as file:
    gramatica = {regra: file.readline().replace('\n','') for regra in range(1,40)}

print(gramatica[1])