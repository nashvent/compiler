from lexical_analyzer.lexer import LexicalAnalyzer

if __name__ == '__main__':
    analyzer = LexicalAnalyzer()

    token = []
    lexeme = []
    row = []
    column = []

    f= open('program_example.aud','r')
    contents = f.read()
    tokens, lexemes, lines, columns = analyzer.tokenize(contents)
    