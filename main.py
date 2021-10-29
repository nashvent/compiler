from Lexer.lexer import LexicalAnalyzer
from Parser.parse import parse_words
from symbols import grammar_text, token_rules

if __name__ == '__main__':
    analyzer = LexicalAnalyzer()

    token = []
    lexeme = []
    row = []
    column = []

    f= open('program_example.aud','r')
    contents = f.read()
    tokens, lexemes, lines, columns = analyzer.tokenize(token_rules, contents)
    
    print("tokens", tokens)
    
    words = ["id", "+", "id","+"]
    result = parse_words(grammar_text, words)