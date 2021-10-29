
token_rules = [
    ('AUD', r'aud'),            # aud type
    ('INT', r'int'),            # int
    ('FLOAT', r'float'),        # float
    ('IF', r'if'),              # if
    ('ELSE', r'else'),          # else
    ('WHILE', r'while'),        # while
    ('READ', r'read'),          # read
    ('PRINT', r'print'),        # print
    ('STRING', r'(\".+\"|\'.+\')'),     # STRING
    ('LBRACKET', r'\('),        # (
    ('RBRACKET', r'\)'),        # )
    ('LBRACE', r'\{'),          # {
    ('RBRACE', r'\}'),          # }
    ('COMMA', r','),            # ,
    ('PCOMMA', r';'),           # ;
    ('OPREL', r'(==|!=|<=|>=|\|\||&&|\=|<|>)'),  # == != <= => || && = < >
    ('PLUS', r'\+'),            # +
    ('MINUS', r'-'),            # -
    ('MULT', r'\*'),            # *
    ('DIV', r'\/'),             # /
    ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
    ('INTEGER_CONST', r'\d(\d)*'),          # INT
    ('ID', r'[a-zA-Z0-9]\w*'),     # IDENTIFIERS
    ('NEWLINE', r'\n'),         # NEW LINE
    ('SKIP', r'[ \t]+'),        # SPACE and TABS
    ('COMMENT', r'#.*'),        # LINE COMMENTS
    ('MISMATCH', r'.'),         # ANOTHER CHARACTER
]

grammar_text = (
    "E -> T E'\n"
    "E' -> + T E' | ε\n"
    "T -> F T'\n"
    "T' -> * F T' | ε\n"
    "F -> ( E ) | id"
)