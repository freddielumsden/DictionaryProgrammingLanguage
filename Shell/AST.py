import throw_error


def ast(tokenized_line):
    main = []
    layer_num = 0
    for i in tokenized_line:
        if i == ("O_BRACKET", None):
            layer_num += 1
            exec(
                "main" + "".join(["[-1]" for i in range(layer_num-1)]) + ".append([])")
        elif i == ("C_BRACKET", None):
            layer_num -= 1
        else:
            name = '"' + str(i[0]) + '"'
            value = '"' + str(i[1]) + '"'
            exec("main" + "".join(["[-1]" for i in range(layer_num)]
                                  ) + ".append((" + name + ", " + value + "))")
    return main


def prettifyAst(ast, starting_tabs=""):
    string_ast = ""
    tabs = starting_tabs
    for i in ast:
        if isinstance(i, tuple):
            string_ast += tabs + i[0] + " : " + i[1] + "\n"
        else:
            tabs += "\t"
            string_ast += tabs + "[\n" + prettifyAst(i, tabs) + tabs + "]\n"
            tabs = tabs[:-1]
    return string_ast


if __name__ == '__main__':
    print('Welcome to the Felicity ast "creator"!')
    import lexer
    while True:
        line = input('>>> ')
        tokenized_line = lexer.lex(line)
        if tokenized_line:
            main = ast(tokenized_line)
            pretty_ast = prettifyAst(main)
            print(pretty_ast, end='')
