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

actions = pd.read_csv('Actions2.csv')
goto = pd.read_csv('GoTo.csv')



with open('gramatica-Mgol.txt') as file:
    gramatica = {regra: file.readline().replace('\n','') for regra in range(0,39)}

with open("FONTE.alg", "r") as f:
    arquivo = f.read()


def action(s,a):
  acao = actions.at[s,a]
  return acao


def trata_Erro(pilha, acao, a):
    if acao == "e0":
        print("Tratamento para o erro e0")
        pilha.append("inicio")
        pilha.append(2)
        return pilha, a
    elif acao == "e1":
        print("Tratamento para o erro 1")
    elif acao == "e2":
        print("Tratamento para o Erro 2")
    else:
        print(f"Panic Mode Ativado: Erro tipo {acao}")
        pilha, a = panicMode(pilha, a)
        return pilha, a


def panicMode(apilha, a):
    while(a.classe != "EOF"):
        npilha = apilha.copy()
        while (len(npilha) > 0):
            acao = action(npilha[-1],a.classe)
            if(acao[0] != "e"):
                return npilha, a
            npilha.pop()
            npilha.pop()
        a = util.scanner2(arquivo)
    return []
                
def error_acao(pilha, a):
    acao = action(pilha[-1],a.classe)

    

  
def lr_parser(actions, goto):
    global auxFimArq
    pilha = ['EOF',0]
    s = pilha[-1]
    a = util.scanner2(arquivo)

    while(True):
        s = pilha[-1]
        acao = action(s,a.classe)
        if acao[0] == 's':
            pilha.append(a.classe)
            pilha.append(int(acao[1:len(acao)]))
            a = util.scanner2(arquivo)
            if(s == 'EOF'):
                auxFimArq = True
        elif acao[0] == 'r':
            prod = gramatica[int(acao[1:len(acao)])]
            p = prod.split(' ')
            body = p[2:len(p)]
            for i in range(0,len(body)):
                pilha.pop()
                pilha.pop()
            t = pilha[-1]
            pilha.append(p[0])
            pilha.append(int(goto.at[t,p[0]]))
            print(pilha)
            print(prod)
        elif acao[0] == "e":
            print(acao)
            pilha, a = trata_Erro(pilha, acao, a)
            print(pilha)
        elif acao == 'acc':
            break
    
        


lr_parser(actions, goto)

