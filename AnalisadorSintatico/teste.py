import copy
import pandas as pd

#afd = main.AFD_LEX()
#afd.mgol_trans()
listaTokens = []
#simbolos = TabelaSimbolos()
linha = 1
coluna = 1
auxArq = 0
auxFimArq = False
isToken = False
erroLexico = False

def fun():
    actions = pd.read_csv('Actions.csv')
    goto = pd.read_csv('GoTo.csv')


    with open('gramatica-Mgol.txt') as file:
        gramatica = {regra: file.readline().replace('\n','') for regra in range(1,40)}

    print(gramatica[1])

    ip = "ES"
    stack = 9

    print(goto[ip][stack])

    print(gramatica[6])



def lr_parser(actions, goto, pilha):
    pilha = [0]
    estado = pilha[-1]
    a = pilha.peek()
    #while True:
        #acao = actions[a][s]

