from ply import yacc
from lexer import tokens

main = {}


def p_expression_binop(t):
    '''expression : expression PLUS expression
                              | expression MINUS expression
                              | expression TIMES expression
                              | expression DIVIDE expression'''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]


def p_multiply_number_expression(t):
    'expression : NUMBER LPAREN expression RPAREN'
    t[0] = t[1] * (t[3])


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_negagive_number(t):
    'expression : MINUS expression'
    t[0] = t[2] * -1
    # Negative numbers - if a minus sign appears before a number, it inverts the number


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]
    # If there is just a plain number, the expression is the number


def p_string(t):
    'expression : STRING'
    t[0] = t[1][1:-1]
    # If there is a string, the expression is a string


def p_assignment(t):
    'expression : VAR_NAME ASSIGN expression'
    main[t[1]] = t[3]
    t[0] = t[3]
    # Assignment


def p_variable_reference(t):
    'expression : VAR_NAME'
    t[0] = main[t[1]]


def p_print_function(t):
    'expression : PRINT_FUNC ASSIGN expression'
    t[0] = t[3]


def p_input_function(t):
    'expression : VAR_NAME ASSIGN INPUT_FUNC'
    main[t[1]] = input("")
    t[0] = ''


def p_error(t):
    if t is None:  # lexer error
        return
    print(f"Syntax Error: {t.value!r}")


if __name__ == '__main__':
    print("This is the felicity parser. To run it, just run the\nfile called main.py, which will lex the code first.")
else:
    parser = yacc.yacc()
