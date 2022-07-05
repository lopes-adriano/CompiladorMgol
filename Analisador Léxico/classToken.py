class Token:
    def __init__(self, classe, lexema, tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def __repr__(self):
        return f'Token(classe:{self.classe}, lexema:{self.lexema}, tipo:{self.tipo})'