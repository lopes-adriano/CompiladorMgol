import fabricaTokens
from classToken import Token

class TabelaSimbolos:

    def __init__(self):
        self.tabelaSimbolos = {}
        reservadas = ["inicio", "varinicio", "varfim", "escreva", "leia", "se", "entao", "fimse", "fim", "inicio", "lit"
        "real", "inteiro", "faca", "enquanto", "fimenquanto"]
        for aux in reservadas:
            obj = Token(aux, aux, aux)
            self.tabelaSimbolos[aux] = obj

    def addSimbolo(self, token):
        self.tabelaSimbolos[token.lexema] = token


test = TabelaSimbolos()

print(test.tabelaSimbolos["faca"])
pernam = Token("id", "pernambuco", "NULO")
test.addSimbolo(pernam)
print(test.tabelaSimbolos)

