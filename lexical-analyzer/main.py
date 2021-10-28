from buffer import Buffer
from lexer import LexicalAnalyzer

if __name__ == '__main__':
    Buffer = Buffer()
    analyzer = LexicalAnalyzer()

    token = []
    lexeme = []
    row = []
    column = []

    for i in Buffer.load_buffer('program_example.aud'):
        tkn, lex, lin, col = analyzer.tokenize(i)
        token += tkn
        lexeme += lex
        row += lin
        column += col