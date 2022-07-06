from lib2to3.pgen2.token import tok_name
from classToken import Token
from tabulate import tabulate

class TabelaSimbolos:

    def __init__(self):
        self.tabelaSimbolos = []
        reservadas = ["inicio", "varinicio", "varfim", "escreva", "leia", "se", "entao", "fimse", "fim", "inicio", "lit",
        "real", "inteiro", "faca", "enquanto", "fimenquanto"]
        for aux in reservadas:
            obj = Token(aux, aux, aux)
            self.tabelaSimbolos.append(obj)
    
    def showTable(self):
        print(tabulate(self.tabelaSimbolos, headers=['Lexema', 'Classe', 'Tipo'], tablefmt='github'))
    
    def checkSimbolo(self, lexema):
        for token in self.tabelaSimbolos:
            if lexema in token:
                return True

    def addSimbolo(self, token):
        if self.checkSimbolo(token.lexema):
            return False
        else:
            self.tabelaSimbolos.append(token)
            return True
