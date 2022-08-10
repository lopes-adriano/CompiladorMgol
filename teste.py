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
    gramatica = {regra: file.readline().replace('\n','') for regra in range(0,39)}

with open("FONTE.alg", "r") as f:
    arquivo = f.read()


def action(s,a):
  acao = actions.at[s,a]
  return acao
  
  
def lr_parser(actions, goto):
    global auxFimArq
    pilha = ['EOF',0]
    s = pilha[-1]
    a = util.scanner(arquivo)
    while(True):
        s = pilha[-1]
        acao = action(s,a.classe)
        if acao[0] == 's':
            pilha.append(int(acao[1:len(acao)]))
            a = util.scanner(arquivo)
            if(a.classe == "fim"):
                auxFimArq = True
        elif acao[0] == 'r':
            prod = gramatica[int(acao[1:len(acao)])]
            p = prod.split(' ')
            body = p[2:len(p)]
            for i in range(0,len(body)):
                pilha.pop()
            t = pilha[-1]
            pilha.append(int(goto.at[t,p[0]]))
            print(prod)
        elif acao == 'acc':
            print('DEU CERTO PORRA')
            break
    
        



lr_parser(actions, goto)

def testeBruto():
    print(actions["varinicio"][2])

#testeBruto()
