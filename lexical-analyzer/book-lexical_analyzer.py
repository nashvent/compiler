class Tag:
    NUM = 256
    ID = 257
    TRUE = 258
    FALSE = 259

class Token:
    def __init__(self, tag):
        self.tag = tag

class Num(Token):
    def __init__(self, value):
        super().__init__(Tag.NUM)
        self.value = value

class Word(Token):
    def __init__(self, tag, lexeme):
        super().__init__(tag)
        self.lexeme = lexeme

class Character:
    @staticmethod
    def isDigit(val):
        return True

    @staticmethod
    def isLetter(val):
        return True
    
    @staticmethod
    def isLetterOrDigit(val):
        return True
    
    @staticmethod
    def digit(look):
        return look

def strToList(strng):
    return list(input)
def listToStr(lst):
    return ''.join(lst)

class Lexer:
    line = 1
    peek = ""
    words = {}

    def reserve(self, t: Word):
        self.words[t.lexeme] = t

    def __init__(self):
        self.reserve(Word(Tag.TRUE, "true"))
        self.reserve(Word(Tag.FALSE, "false"))


    def explore(self, input) -> Token:
        
        chars = strToList(input)
        while(len(chars)):
            self.peek = chars.pop(0)
            if(self.peek == '' or self.peek == '\t'):
                continue
            elif (self.peek == '\n'):
                self.line += 1
            else:
                break
            
        if(Character.isDigit(self.peek)): # is digit
            v = 0
            while(True):
                v = 10*v + Character.digit(self.peek, 10)
                self.peek = chars.pop(0)
                if(Character.isDigit(self.peek) == False):
                    return Num(v), listToStr(chars) 
        if(Character.isLetter(self.peek)):
            buffer = ''
            while(True):
                buffer += self.peek
                self.peek = chars.pop(0)
                if(Character.isLetterOrDigit(self.peek) == False):
                    break
            word = Word(Tag.ID, buffer)
            self.words[buffer] = word
            return word 
        token = Token(self.peek)
        self.peek = ''
        return token

