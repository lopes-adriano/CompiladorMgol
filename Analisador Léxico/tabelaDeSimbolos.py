import fabricaTokens
import classToken

class TabelaSimbolos:

    def __init__(self):
        self.tabelaSimbolos = {}
        reservadas = ["inicio", "varinicio", "varfim", "escreva", "leia", "se", "entao", "fimse", "fim", "inicio", "lit"
        "real", "inteiro", "faca", "enquanto", "fimenquanto"]
        for aux in reservadas:
            obj = classToken(aux, aux, aux)
            self.tabelaSimbolos[aux] = obj

    def addSimbolo(self, token):
        self.tabelaSimbolos[token.lexema] = token


test = TabelaSimbolos()

print(test.tabelaSimbolos["faca"])
test.addID("pernambuco")
print(test.tabelaSimbolos)

