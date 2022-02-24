from ply import lex
import re

# Keywords
regexes_and_keywords = {
    r'print': 'PRINT_FUNC',
    r'input': 'INPUT_FUNC',
    r'^".*"$|^\'.*\'$': 'STRING',
    r'[a-zA-Z_][a-zA-Z0-9_]*': 'VAR_NAME'
}
# Symbols
symbols = ['COMMENT',
          'SPACE',
          'NUMBER',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'LPAREN',
          'RPAREN',
          'ASSIGN'
          ]
tokens = symbols + list(regexes_and_keywords.values())
t_ignore_COMMENT = r'\#.*'
t_SPACE = r'[ ]'
# Gets tokens which don't have to be seperated by spaces
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'\*'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r':'

# Gets tokens which have to be seperated by spaces.

def t_ID():
	
def t_KEYWORD(t):
    r'[^ ]+'
    for regex in regexes_and_keywords:
        if bool(re.match(regex, t.value)):
            t.type = regexes_and_keywords[regex]
            return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character {t.value[0]!r} on line {t.lexer.lineno}")
    t.lexer.skip(1)


t_ignore = ' \t'  # Characters to ignore while lexing

lexer = lex.lex()
if __name__ == '__main__':
    print("Welcome to the felicity lexer.")
    print("Currently, the following characters are available:")
    print(", ".join(tokens))
    text = input("Text to lex: ")
    lexer.input(text)
    for token in lexer:
        print(token)
