from AnalisadorLexico.classToken import Token
from AnalisadorLexico.tabelaDeSimbolos import TabelaSimbolos
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
            return False
    
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

