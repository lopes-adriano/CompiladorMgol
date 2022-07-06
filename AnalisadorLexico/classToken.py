from types import NoneType


class Token:
    def __init__(self, lexema, classe, tipo):
        self.lexema = lexema
        self.classe = classe
        self.tipo = tipo


    def __repr__(self):
        return f'Lexema: {self.lexema}, Classe: {self.classe}, Tipo:{self.tipo}'

    def __iter__(self):
        return iter([self.lexema, self.classe, self.tipo])
    
    def idToken(self, lexema, estado):
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
        classe = self.classes[estado]

        if (estado == 1) or (estado == 6):

            tipo = "inteiro"
        elif (estado == 3)or(estado == 23):
            tipo = "real"
        elif estado == 8:
            tipo = "literal"
        else: 
            tipo = "nulo"
        tok = Token(lexema, classe, tipo)
        return tok
