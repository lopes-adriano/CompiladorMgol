from classToken import Token
from tabelaDeSimbolos import TabelaSimbolos
import colorama
from colorama import Fore


colorama.init(autoreset = True)


class AFD_LEX:
    def __init__(self):
        self.inicial = 0
        self.final = [1,3,6,8,9,11,12,13,14,15,16,17,18,19,20,21,23]
        self.trans = {estado:{} for estado in range(0,26)}
        self.alfabeto = """ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g 
        h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ' , " ; : . ! ? \ * + - / ( ) { } [ ] < > = """.split()
        self.letras = tuple(self.alfabeto[0:52])
        self.digitos = tuple(self.alfabeto[52:62])
        self.outros = tuple(self.alfabeto[62:])
        
    def isValid(self,c, linha, coluna):
        if c in self.alfabeto:
            return True
        else:
            tokenE = Token(c, "ERRO", "NULO")
            print(f'{Fore.YELLOW}{tokenE}')
            print(f'{Fore.YELLOW} Erro Léxico - Caractere inválido na linha {linha}, coluna {coluna-1}.')
            listaTokens.append(tokenE)
    
    def add_trans(self,atual, c, prox):
        nova_trans = {str(c): prox}
        self.trans[atual].update(nova_trans)

    def display_trans(self):
        print(self.trans)

    def mgol_trans(self):

        #Ramo dos Num
        for digito in self.digitos:
            self.add_trans(0,digito, 1)
            self.add_trans(1,digito, 1)
            self.add_trans(2,digito, 3)
            self.add_trans(3,digito, 3)
            self.add_trans(4,digito, 6)
            self.add_trans(5,digito, 6)
            self.add_trans(6,digito, 6)
            self.add_trans(22, digito, 23)
            self.add_trans(23, digito, 23)
            self.add_trans(24, digito, 23)
            self.add_trans(25, digito, 23)
            

            
        self.add_trans(1,'.',2)
        self.add_trans(1,'E',4)  
        self.add_trans(1,'e',4)
        self.add_trans(3,'E',24)  
        self.add_trans(3,'e',24)
        self.add_trans(4,'+', 5)
        self.add_trans(4,'-', 22)
        self.add_trans(24,'+', 25)
        self.add_trans(24,'-', 25)
        

        #Ramo lit
        self.add_trans(0,'"',7)
        self.add_trans(0,"'",7)
        self.add_trans(7,'"',8)
        self.add_trans(7,"'",8)
        self.add_trans(7,' ', 7)
        
        for letra in self.letras:
            self.add_trans(7,letra,7)
        for digito in self.digitos:
            self.add_trans(7,digito,7)  
        for outro in self.outros:
            if(outro !='"' and outro !="'"):
                self.add_trans(7,outro,7)

        #Id
        for letra in self.letras:
            self.add_trans(0,letra,9)
            self.add_trans(9,letra,9)
        for digito in self.digitos:
            self.add_trans(9,digito,9)
        self.add_trans(9,'_',9)

        #Comentário
        self.add_trans(0,'{',10)
        self.add_trans(10,'}',11)
        self.add_trans(10,' ', 10)
        
        for letra in self.letras:
            self.add_trans(10,letra,10)
        for digito in self.digitos:
            self.add_trans(10,digito,10)
        for outro in self.outros:
            if(outro !='{' and outro !="}"):
                self.add_trans(10,outro,10)
        
        #EOF
        self.add_trans(0,'EOF',12)

        #OPR
        self.add_trans(0,'=',13)
        self.add_trans(0,'>',14)
        self.add_trans(14,'=',13)
        self.add_trans(0,'<',15)
        self.add_trans(15,'>',13)
        self.add_trans(15,'=',13)

        #RCB
        self.add_trans(15,'-',16)

        #OPR
        for opm in ['+','-','*','/']:
            self.add_trans(0,opm,17)

        #Abre Parênteses
        self.add_trans(0,'(',18)

        #Fecha Parênteses
        self.add_trans(0,')',19)

        #Ponto e virgula
        self.add_trans(0,';',20)
        self.add_trans(0,',',21)

        #Espaço em branco/Tab/Nova linha
        self.add_trans(0,' ',0)
        self.add_trans(0,'\t',0)
        self.add_trans(0,'\n',0)


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
        if(estado != 11):
            return simbolo
    else:
        if(lexema != " ")and(lexema != "\n")and(lexema != "\t"):
            try:
                token = idToken(lexema, estado)
                if(estado != 11):
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
        print(token)
        print(f"ERRO Léxico Identificado: Linha:{linha}")
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

        if(isToken):
            token = geraToken(lexema, estado)
            simbolos.addSimbolo(token)
            isToken = False
            return token

        elif(erroLexico):
            token = trataErro(estado, c, lexema)
            erroLexico = False

        else:
            moveCoordenada(c)
            if (naoIgnora(c) and afd.isValid(c,linha,coluna)) or estado == 10 or estado == 7:
                lexema = lexema + c
    auxFimArq = True
    token = geraToken("EOF", 12)
    return token


def main():
    with open("FONTE.alg", "r") as f:
        arquivo = f.read()
    while(auxFimArq == False):
        tk_retorno = scanner(arquivo)
        listaTokens.append(tk_retorno)
        print(tk_retorno)

    print("\n\nTABELA DE SIMBOLOS\n\n")
    simbolos.showTable()


main()