from Lexer.lexer import LexicalAnalyzer
from Parser.parse import parse_words
from symbols import grammar_text, token_rules
import sys

if __name__ == '__main__':
    if(len(sys.argv) < 2 ):
        raise Exception("Need input filename as argument")
    filename = sys.argv[1]
    
    analyzer = LexicalAnalyzer()

    token = []
    lexeme = []
    row = []
    column = []


    f= open(filename,'r')
    contents = f.read()
    tokens, lexemes, lines, columns = analyzer.tokenize(token_rules, contents)
    
    print("tokens", tokens)
    
    result = parse_words(grammar_text, tokens)
    