
token_rules = [
    ('aud', r'aud'),            # aud type
    ('int', r'int'),            # int
    ('float', r'float'),        # float
    ('string', r'string'),      # string
    ('null', r'null'),          # null
    ('if', r'if'),              # if
    ('else', r'else'),          # else
    ('while', r'while'),        # while
    ('read', r'read'),          # read
    ('store', r'store'),          # store
    ('string_const', r'(\".+\"|\'.+\')'), # string
    ('lbracket', r'\('),        # (
    ('rbracket', r'\)'),        # )
    ('lbrace', r'\{'),          # {
    ('rbrace', r'\}'),          # }
    ('comma', r','),            # ,
    ('pcomma', r';'),           # ;
    ('assign', r'\='),          # assign
    ('op', r'(==|!=|<=|>=|\|\||&&|\=|<|>)'),  # == != <= => || && = < >
    ('plus', r'\+'),            # +
    ('minus', r'-'),            # -
    ('mult', r'\*'),            # *
    ('div', r'\/'),             # /
    ('float_const', r'\d(\d)*\.\d(\d)*'),   # float constant
    ('int_const', r'\d(\d)*'),          # int constant
    ('id', r'[a-zA-Z0-9]\w*'),     # indentifiers
    ('newline', r'\n'),         # new line
    ('skip', r'[ \t]+'),        # spaces (tabs)
    ('comment', r'#.*'),        # line comments
    ('mismatch', r'.'),         # ANOTHER CHARACTER
]

grammar_text = (
    "PROGRAM -> BLOCK\n"
    "BLOCK -> SENTENCE SENTENCE'\n"
    "SENTENCE' -> pcomma SENTENCE SENTENCE' | ε\n"
    "SENTENCE -> ASSIGN\n"
    "ASSIGN -> TYPE VAR assign EXPR | VAR assign EXPR\n"
    "STORE -> store lbracket EXPR rbracket\n"
    "EXPR -> TERM TERM' | READ\n"
    "TERM' -> plus TERM TERM' | minus TERM TERM' | ε\n"
    "TERM -> PRIMARY FACTOR\n"
    "FACTOR -> mult ELEMENT FACTOR | div ELEMENT FACTOR | ε\n"
    "PRIMARY -> minus PRIMARY | ELEMENT\n"
    "ELEMENT -> lbracket EXPR rbracket | VAR | CONST\n"
    "READ -> read lbracket ELEMENT rbracket\n"
    "CONST -> string_const | float_const | int_const\n"
    "TYPE -> aud | int | float | string\n"
    "VAR -> id"
)


# grammar_text = (
#     "PROGRAM -> BLOCK pcomma\n"
#     "BLOCK -> pcomma | id assign EXPR pcomma | while P_EXPR BLOCK | READ | lbrace PROGRAM rbrace\n"
#     "P_EXPR -> lbracket EXPR rbracket\n"
#     "EXPR -> ADD_EXPR\n"
#     "ADD_EXPR -> plus MULT_EXPR | minus MULT_EXPR\n"
#     "MULT_EXPR -> mult PRIMARY | div PRIMARY | PRIMARY\n"
#     "PRIMARY -> id | CONST | lbrace EXPR rbrace | plus PRIMARY | minus PRIMARY\n"
#     "READ -> read lbracket ELEMENT rbracket pcomma\n"
#     "CONST -> string_const | float_const | int_const"
# )

# grammar_text = (
#     "PROGRAM -> BLOCK\n"
#     "BLOCK -> lbrace INSTRS rbrace\n"
#     "INSTRS -> INSTR | ε\n"
#     "INSTR -> EXPR pcomma | if lbracket EXPR rbracket INSTR | while lbracket EXPR rbracket INSTR | BLOCK\n"
#     "EXPR -> REL assign EXPR | REL\n"
#     "REL -> ADIC\n"
#     "ADIC -> plus TERM | minus TERM\n"
#     "TERM -> mult PRIMARY | div PRIMARY | PRIMARY\n"
#     "PRIMARY -> id | CONST | lbrace EXPR rbrace | plus PRIMARY | minus PRIMARY\n"
#     "READ -> read lbracket ELEMENT rbracket pcomma\n"
#     "CONST -> string_const | float_const | int_const"
# )