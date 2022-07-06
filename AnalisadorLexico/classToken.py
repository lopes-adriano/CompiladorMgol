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