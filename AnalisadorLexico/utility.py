from classToken import Token

linha = 1
coluna = 1
listaTokens = []

def naoIgnora(c):
    if(c != " ")and(c != "\n")and(c != "\t"):
        return True
    return False

def trataErro(estado, c, lexema):
    tipoErro = ""
    global linha
    global coluna
    global listaTokens
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
        print(token)
        print(f"ERRO Léxico Identificado: Linha:{linha}")
        print(f"Erro do tipo {tipoErro}, não foi possivel identificar esse Token devido ao lexema incompleto:({lexema})")
        if(estado != 11):
            listaTokens.append(token)

def moveCoordenada(c):
    global coluna
    global linha
    if(c == "\n"):
        coluna = 1
        linha += 1
    elif(c == "\t"):
        coluna += 4
    else:
        coluna += 1  