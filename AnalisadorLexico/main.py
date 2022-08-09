from classToken import Token
from tabelaDeSimbolos import TabelaSimbolos
from afd import *
import colorama
from colorama import Fore


colorama.init(autoreset = True)

afd = AFD_LEX()
afd.mgol_trans()
listaTokens = []
simbolos = TabelaSimbolos()
linha = 1
coluna = 1
auxArq = 0
auxFimArq = False
isToken = False
erroLexico = False


def moveCoordenada(c):
    global auxArq
    global coluna
    global linha

    auxArq += 1
    if(c == "\n"):
        coluna = 1
        linha += 1
    elif(c == "\t"):
        coluna += 4
    else:
        coluna += 1  


def idToken(lexema, estado):
    classes = {
        1: "Num", 
        3: "Num",
        6: "Num",
        8: "Lit",
        9: "id", 
        11: "comentário",
        12: "EOF",
        13: "OPR",
        14: "OPR",
        15: "OPR",
        16: "RCB",
        17: "OPM",
        18: "AB_P",
        19: "FC_P",
        20: "PT_V",
        21: "VIR",
        23: "Num"
    }
    classe = classes[estado]
    if (estado == 1)or(estado == 6):
        tipo = "inteiro"
    elif (estado == 3)or(estado == 23):
        tipo = "real"
    elif estado == 8:
        tipo = "literal"
    else: 
        tipo = "NULO"
    tok = Token(lexema, classe, tipo)
    return tok


def geraToken(lexema, estado):
    global listaTokens
    global simbolos
    if(simbolos.checkSimbolo(lexema)):
        simbolo = simbolos.getToken(lexema)
        return simbolo
    else:
        if(lexema != " ")and(lexema != "\n")and(lexema != "\t"):
            try:
                token = idToken(lexema, estado)
                return token
            except KeyError:
                print("Não foi possivel gerar Token")
                print(f"Estado:{estado}   Lexema:{lexema}")
                token = Token(lexema, "ERRO", "NULL")
                return token


def trataChar(estado, c):
    global erroLexico
    global isToken
    try: 
        novoEstado = afd.trans[estado][c]
        return novoEstado
    except:
        if(eFinal(estado)):
            isToken = True
            return estado
        else:
            if(naoIgnora(c)):
                erroLexico = True
            return estado


def eFinal(estado):
    if estado in afd.final:
        return True
    return False


def naoIgnora(c):
    if(c != " ")and(c != "\n")and(c != "\t"):
        return True
    return False


def trataErro(estado, c, lexema):
    tipoErro = ""
    global linha
    global coluna
    if(estado in range(1, 6)or(estado in range(22, 25))):
        tipoErro = "Num"
    elif(estado in range(7, 8)):
        tipoErro = "Literal"
    elif(estado == 9):
        tipoErro = "Id"
    elif(estado in range(10, 11)):
        tipoErro = "Comentario"
    else:
        tipoErro = "Lexico"
    if(naoIgnora(c)and(lexema != "")):
        token = Token(lexema, "ERRO", "NULO")
        print(f"{Fore.YELLOW}ERRO Léxico Identificado: Linha:{linha}")
        return token


def scanner(arquivo):
    global auxFimArq
    global isToken
    global erroLexico
    lexema = ""
    estado = 0

    while(auxArq < len(arquivo)):
        c = arquivo[auxArq]
        estado = trataChar(estado, c)

        if((not afd.isValid(c,linha,coluna)) and (naoIgnora(c)) and lexema == ""):
            moveCoordenada(c)
            print(f'{Fore.YELLOW} Erro Léxico - Caractere inválido na linha {linha}, coluna {coluna-1}.')
            erroLexico = False
            tokenE = Token(c, "ERRO", "NULO")
            return tokenE

        if((not afd.isValid(c,linha,coluna)) and (naoIgnora(c)) and ((estado == 7) or (estado == 10))):
            print(f'{Fore.YELLOW} Erro Léxico - Caractere inválido na linha {linha}, coluna {coluna-1}.')
            erroLexico = False
            tokenE = Token(c, "ERRO", "NULO")
            print(tokenE)

        if(isToken):
            token = geraToken(lexema, estado)
            simbolos.addSimbolo(token)
            isToken = False
            return token

        elif(erroLexico):
            token = trataErro(estado, c, lexema)
            erroLexico = False
            return token

        #elif((not afd.isValid(c,linha,coluna)) and (naoIgnora(c))):
            #moveCoordenada(c)
           # print(f'{Fore.YELLOW} Erro Léxico - Caractere inválido na linha {linha}, coluna {coluna-1}.')
           # if(not (estado == 10 or estado == 7)):
              #  tokenE = Token(c, "ERRO", "NULO")
             #   return tokenE
            
        else:
            moveCoordenada(c)
            if naoIgnora(c) or estado == 10 or estado == 7:
                lexema = lexema + c

    auxFimArq = True
    token = geraToken("EOF", 12)
    return token


def main():
    with open("FONTE.alg", "r") as f:
        arquivo = f.read()
    while(auxFimArq == False):
        tk_retorno = scanner(arquivo)
        if(tk_retorno.classe != "comentário"):
            listaTokens.append(tk_retorno)
            print(tk_retorno)

    print("\n\nTABELA DE SIMBOLOS\n\n")
    simbolos.showTable()


main()