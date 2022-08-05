from AnalisadorLexico.classToken import Token
from AnalisadorLexico.tabelaDeSimbolos import TabelaSimbolos
from AnalisadorLexico.utility import *
from AnalisadorLexico.afd import AFD_LEX


afd = AFD_LEX()
afd.mgol_trans()
listaTokens = []
simbolos = TabelaSimbolos()
linha = 1
coluna = 1
isToken = False
erroLexico = False
estado = 0
lexema = ""

def geraToken(lexema, estado):
    global listaTokens
    global simbolos
    if(simbolos.checkSimbolo(lexema)):
        simbolo = simbolos.getToken(lexema)
        if(estado != 11):
            listaTokens.append(simbolo)
            print(simbolo)
    else:
        if(lexema != " ")and(lexema != "\n")and(lexema != "\t"):
            try:
                token = Token.idToken(lexema, estado)
                if(estado != 11):
                    listaTokens.append(token)
                    print(token)
            except KeyError:
                print("Não foi possivel gerar Token")
                print(f"Estado:{estado}   Lexema:{lexema}")

print("\n\nInicio do Codigo do SCANNER\n\n")
with open("FONTE.alg", "r") as f:
    arquivo = f.read()
for c in arquivo:
    moveCoordenada(c)
    if(c == ""):
        geraToken(lexema, estado)
    estado = afd.trataChar(estado, c)
    if(isToken):
        geraToken(lexema, estado)
        lexema = ""
        estado = 0
        isToken = False
        if naoIgnora(c) and afd.isValid(c,linha,coluna):
            lexema = lexema + c
            estado = afd.trataChar(estado, c)
    elif(erroLexico):
        trataErro(estado, c, lexema)
        lexema = ""
        estado = 0
        erroLexico = False
        if(naoIgnora(c)):
            lexema = lexema + c
            estado = afd.trataChar(estado, c)
    else:
        if (naoIgnora(c) and afd.isValid(c,linha,coluna)) or estado == 10 or estado == 7:
            lexema = lexema + c
if(afd.eFinal(estado)):
    geraToken(lexema, estado)
else:
    trataErro(estado, c, lexema)
geraToken("EOF", 12)
for t in listaTokens:
    simbolos.addSimbolo(t)
#print("\n\nLista de Tokens\n\n")
#for t in listaTokens:
    #print(t)
print("\n\nTABELA DE SIMBOLOS\n\n")
simbolos.showTable()