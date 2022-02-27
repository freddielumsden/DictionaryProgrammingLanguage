import lexer
import ast
import parser
import throw_error

def check_error():
	if throw_error.error_thrown:
		return True

line = input(">>> ")
while line != "":
	line = input(">>> ")
	lexed_line = lexer.lex(line)
	ast = ast.ast(lexed_line)
	parser.parse(ast)
	if check_error():
		break