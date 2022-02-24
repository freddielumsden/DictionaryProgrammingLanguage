import lexer
import converter
import time
file_name = "examplefile"  # input("File Name: ")
with open(file_name, 'r') as f:
    file = f.read()
lexed_file = lexer.lexer(file)
if lexed_file != None:
	print("Lexed File:", lexed_file)
	converted_file = converter.converter(lexed_file)
	print("Converted File:", converted_file)
time.sleep(10)