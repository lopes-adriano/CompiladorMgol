import copy
from numpy import append
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

def acao(acao, a, pilha):
    estado = ""
    ant_est = 0
    gram = ""
    nregra = ""
    if(acao[0] == "s"):
        pilha.append(a)
        for c in range(1, len(acao)):
            estado += acao[c]
        pilha.append(int(estado))
        return pilha
    if(acao[0] == "r"):
        for c in range(1, len(acao)):
            nregra += acao[c]
        gram = gramatica[int(nregra)]
        gram = gram.split(" ")
        for c in range(0, (len(gram)-2)*2):
            pilha.pop()
        ant_est = pilha[len(pilha)-1]
        ant_est = goto[gram[0]][int(ant_est)]
        pilha.append(gram[0])
        pilha.append(ant_est)
        return pilha

def lr_parser(actions, goto):
    pilha = [0]
    estado = 0
    while(True):

        estado = pilha[len(pilha)-1]

        a = util.scanner(arquivo).classe
        print(a)
        print(estado)
        print(actions[a][estado])
        pilha = acao(actions[a][estado], a, pilha)
        print(pilha)



lr_parser(actions, goto)

def testeBruto():
    print(actions["varinicio"][2])

#testeBruto()
