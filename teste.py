import copy
from numpy import append
import pandas as pd
from colorama import Fore
from AnalisadorLexico import afd, util, tabelaDeSimbolos


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



with open('gramatica-Mgol.txt', 'r') as file:
    gramatica = {regra: file.readline().replace('\n','') for regra in range(0,39)}

with open("FONTE.alg", "r") as f:
    arquivo = f.read()

with open('erros.txt', 'r', encoding='utf-8') as file:
    erros = {e: file.readline().replace('\n','') for e in range(0,77)}


def action(s,a):
  acao = actions.at[s,a]
  return acao


def printErro(acao, a):
    global erros
    e = erros.get(int(acao[1:len(acao)])-1)
    print(f'{Fore.RED}{e} \nlinha: {util.linha} coluna: {util.coluna-len(a.lexema)}'.replace('{tok}', a.lexema))

    
def trata_Erro(apilha, acao, a):
    pilha = copy.deepcopy(apilha)
    printErro(acao, a)
    if acao == "e0":
        print(f"\n-----Erro detectado\n-----Tratamento para o erro {acao}")
        pilha.append("inicio")
        pilha.append(2)
        return pilha, a
    if acao == "e1":
        while(a.classe != "EOF"):
            a = util.scanner2(arquivo)
        return pilha, a
    elif acao == "e2":
        print(f"\n-----Erro detectado\n-----Tratamento para o erro {acao}")
        pilha.append("varinicio")
        pilha.append(4)
        return pilha, a
    elif acao == "e17":
        pilha.append("ab_p")
        pilha.append(46)
        return pilha, a
    elif (acao == "e55")or(acao == "e56")or(acao == "e16")or(acao == "e45")or(acao == "e46"):
        print(f"\n-----Erro detectado\n-----Tratamento para o erro {acao}")
        while(len(pilha)>0):
            if(pilha[-2] == "se"):
                pilha.pop()
                pilha.pop()
                pilha.append('CAB')
                pilha.append(14)
                if(a.classe == "entao"):
                    a = util.scanner2(arquivo)
                break
            elif(pilha[-2] == "repita"):
                pilha.pop()
                pilha.pop()
                pilha.append('CABR')
                pilha.append(15)
                break
            pilha.pop()
            pilha.pop()
        return pilha, a
    else:
        print(f"\n-----Erro detectado. Panic Mode Ativado\n-----Tratamento para o erro {acao}")
        pilha,a = panicMode(pilha, a)
        return pilha, a

def redux(apilha, a):
    pilha = copy.deepcopy(apilha)
    acao = action(pilha[-1],a.classe)
    prod = gramatica[int(acao[1:len(acao)])]
    p = prod.split(' ')
    body = p[2:len(p)]
    for i in range(0,len(body)):
        pilha.pop()
        pilha.pop()
    t = pilha[-1]
    pilha.append(p[0])
    pilha.append(int(goto.at[t,p[0]]))
    print(prod)
    return pilha

def panicMode(apilha, a):
    while(a.classe != "EOF"):
        npilha = copy.deepcopy(apilha)
        while npilha[-1] != "EOF":
            acao = action(npilha[-1],a.classe)
            if(acao[0] != "e"):
                return npilha, a
            npilha.pop()
            npilha.pop()
        a = util.scanner2(arquivo)
    return [], a
                
def error_acao(pilha, a):
    acao = action(pilha[-1],a.classe)

    

  
def lr_parser(actions, goto):
    global auxFimArq

    pilha = ['EOF',0]
    s = pilha[-1]
    a = util.scanner2(arquivo)

    while(pilha):
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

            print(prod)
            #print(util.linha)
        elif acao[0] == "e":
            print(acao)
            pilha, a = trata_Erro(pilha, acao, a)
          #  print(pilha)
        elif acao == 'acc':
            break   
        print(pilha)
        


lr_parser(actions, goto)

