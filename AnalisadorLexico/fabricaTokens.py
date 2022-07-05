from classToken import Token

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
        21: "VIR"
    }
    classe = self.classes[estado]
    if estado == 1:
        tipo = "inteiro"
    elif (estado == 3)or(estado == 6):
        tipo = "real"
    elif estado == 8:
        tipo = "literal"
    else: 
        tipo = "NULO"
    token = Token(classe, lexema, tipo)