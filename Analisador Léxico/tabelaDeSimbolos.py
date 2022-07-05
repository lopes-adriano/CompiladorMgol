class TabelaSimbolos:

    def __init__(self):
        self.tabelaSimbolos = {}
        reservadas = ["inicio", "varinicio", "varfim", "escreva", "leia", "se", "entao", "fimse", "fim", "inicio", "lit"
        "real", "inteiro", "faca", "enquanto", "fimenquanto"]
        for aux in reservadas:
            self.tabelaSimbolos[aux] = {"lexema":aux, "token":aux, "tipo":"vazio"}

    def addID(self, lexema):
        self.tabelaSimbolos[lexema] = {"lexema":lexema, "token":"id", "tipo":"vazio"}


test = TabelaSimbolos()

print(test.tabelaSimbolos["faca"])
test.addID("pernambuco")
print(test.tabelaSimbolos)

