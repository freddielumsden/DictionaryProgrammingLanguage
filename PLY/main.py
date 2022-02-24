import parser # Initializes the parser

while True:
	line = input(">>> ")
	print(parser.parser.parse(line))