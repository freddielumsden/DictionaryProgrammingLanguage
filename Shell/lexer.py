class Token():
    def __init__(self, ID, value=None):
        self.ID = ID
        self.value = value


def lex(line):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    symbols = {'#': 'COMMENT',
               '+': 'ADD',
               '-': 'SUBTRACT',
               '*': 'MULTIPLY',
               '/': 'DIVIDE',
               '(': 'O_BRACKET',
               '{': 'O_BRACKET',
               }
    main = {}
    builtins = [# Built-in variables
                '__builtins__',
                'main',
                # Built-in functions
                'print',
                'input',

            ]
    tokenized_line = []
    # Remove comments from line
    try:
        line = line[:line.index('#')]
    except:
        pass
    for pos, char in enumerate(line):
        # Check if previous character was a number, if so skip to next character
        if line[pos-1] in numbers and char in numbers and not pos == 0:
            continue
        # Try to append the character as a symbol to the tokenized line...
        try:
            tokenized_line.append(Token(symbols[char]))
        # ... Otherwise
        except:
            # If the character is a number or a decimal place
            if char in numbers:
                number = char
                index = pos
                while True:
                    index += 1
                    try:
                        if line[index] in numbers:
                            number += line[index]
                        else:
                            break
                    except:
                        break
                if '.' in number:
                    number = float(number)
                else:
                    number = int(number)
                tokenized_line.append(Token("NUMBER", number))
    return ",\n".join([i.ID + " : " + str(i.value) for i in tokenized_line])


if __name__ == '__main__':
    print("Welcome to the lexer of felicity!")
    while True:
        line = input(">>> ")
        if line == "":
            break
        print(lex(line))
