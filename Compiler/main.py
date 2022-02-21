import lexer

file_name = input("File Name: ")
with open(file_name, 'r') as f:
    file = f.read()
lexed_file = lexer.lexer(file)
print("Lexed File:", file)
