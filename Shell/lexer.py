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
               '/': 'DIVIDE'
               }
    keywords = []
    tokenized_line = []
    # Remove comments from line
    try:
        line = line[:line.index('#')]
    except:
        pass
    for pos, char in enumerate(line):
        try:
            tokenized_line.append(Token(symbols[char]))
        except:
            if char in numbers:
                number = char
                index = pos
                while True:
                    index += 1
                    if line[index] in numbers:
                        number += line[index]
                    else:
                        break
                if '.' in number:
                    number = float(number)
                else:
                    number = int(number)
                tokenized_line.append(Token("NUMBER", number))
    return "".join([i.ID + "," + str(i.value) for i in tokenized_line])


if __name__ == '__main__':
    print("Welcome to the lexer of felicity!")
    while True:
        line = input(">>> ")
        if line == "":
            break
        print(lex(line))
