import copy
import pandas as pd
from AnalisadorLexico import afd, classToken, util, tabelaDeSimbolos


lex = afd.AFD_LEX()
lex.mgol_trans()
listaTokens = []
simbolos = tabelaDeSimbolos.TabelaSimbolos()
linha = 1
coluna = 1
auxArq = 0
auxFimArq = False
isToken = False
erroLexico = False

actions = pd.read_csv('Actions.csv')
goto = pd.read_csv('GoTo.csv')


with open('gramatica-Mgol.txt') as file:
    gramatica = {regra: file.readline().replace('\n','') for regra in range(1,40)}

with open("FONTE.alg", "r") as f:
    arquivo = f.read()

print(gramatica[1])

ip = "ES"
stack = 9

print(goto[ip][stack])

print(gramatica[6])



def lr_parser(actions, goto):
    pilha = [0]
    estado = pilha[-1]
    a = util.scanner(arquivo).classe
    print(a)
    
    print(actions[a][estado])

lr_parser(actions, goto)

