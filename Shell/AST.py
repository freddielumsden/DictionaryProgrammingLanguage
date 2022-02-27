import throw_error


def loopAst(element):
	# loopAst() uses recursion to aid stringAst in looping through all elements.
	if isinstance(element, list):
		pass


def stringAst(ast):
	# stringAst() takes a list of token_objs and returns a string that can be printed
	for element in ast:
		loopAst(element)


class Expression():
	def __init__(self, content, name=None):
		self.expression = []
		self.content = content
		self.tokens = [(i.ID, i.value) for i in self.content]
		if name is not None:
			self.name = name

def expressionize(expression):  # With want for a better name ;)
	tokens = expression.tokens
	content = expression.content
	if tokens!=None:
		# Checks if any open brackets are left to expressionize
		try:
			open_bracket_pos = tokens.index(("O_BRACKET", None))
		except:
			return tokens
		# Throws an exception if there isn't a closed bracket,
		# because we have already ensured that there are open brackets left.
		try:
			close_bracket_pos = (
				len(tokens) - tokens[::-1].index(("C_BRACKET", None))) - 1
		except:
			throw_error.error("Bracket never closed")
			return
		sub_expression = Expression(
			content[open_bracket_pos:close_bracket_pos])
		expressionize(sub_expression)
		
		
		expression.expression.append(
			self.content[:open_bracket_pos] + [expression.content])
		del self.content[:close_bracket_pos]
		del self.tokens[:close_bracket_pos]

def getID(list):
	id_list = []
	for i in list:
		try:
			id_list.append(i.ID)
		except:
			id_list.append(getID(i))
	return id_list

def ast(lexed_line, line):
	main = Expression(lexed_line, "main")
	main.expressionize(line)
	return getID(main.content)


if __name__ == '__main__':
	print('Welcome to the Felicity ast "creator"!')
	import lexer
	while True:
		line = input('>>> ')
		tokenized_line = lexer.lex(line)
		if tokenized_line:
			print(ast(tokenized_line, line))
