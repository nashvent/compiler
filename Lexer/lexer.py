import re
class LexicalAnalyzer:
    lin_num = 1
    
    def tokenize(self,token_rules, code):
        rules = token_rules

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        token = []
        lexeme = []
        line = []
        column = []

        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'newline':
                lin_start = m.end()
                self.lin_num += 1
            elif token_type == 'skip': # or token_type == 'COMMENT':
                continue
            elif token_type == 'mismatch':
                raise RuntimeError('%r unexpected token on line %d' % (token_lexeme, self.lin_num))
            else:
                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    line.append(self.lin_num)
                    # print('<{0},\'{1}\'>'.format(token_type, token_lexeme))

        return token, lexeme, line, column