import throw_error


class Token():
	def __init__(self, ID, value=None):
		self.ID = ID
		self.value = value


def lex(line):
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
	symbols = {'#': Token('COMMENT'),
			   '+': Token('ADD'),
			   '-': Token('SUBTRACT'),
			   '*': Token('MULTIPLY'),
			   '/': Token('DIVIDE'),
			   '(': Token('O_BRACKET'),
			   '{': Token('O_BRACKET'),
			   '[': Token('O_BRACKET'),
			   ')': Token('C_BRACKET'),
			   '}': Token('C_BRACKET'),
			   ']': Token('C_BRACKET')
			   }
	builtins = {  # Built-in variables
		'builtins': Token('VAR', 'builtins'),
		'main': Token('DICT', 'main'),
		'conventions': Token('DICT', 'conventions'),
		# Built-in functions
		'print': Token('FUNC', 'print'),
		'input': Token('FUNC', 'input')
	}
	words = numbers + list(symbols.keys()) + list(builtins.keys())
	tokenized_line = []
	# Remove comments from line
	try:
		line = line[:line.index('#')]
	except:
		pass
	continue_ = 0
	for pos, char in enumerate(line):
		if continue_ != 0:
			continue_ -= 1
			continue
		# Check if the character is allowed
		if char not in words + ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
								'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
								'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
								'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '"', "'"]:
			throw_error.error('Character not recognised', pos)
			return
		# Check if previous character was a number, if so skip to next character
		if line[pos-1] in numbers and char in numbers and not pos == 0:
			continue
		# Try to append the character as a symbol to the tokenized line...
		try:
			tokenized_line.append(symbols[char])

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
			else:
				if char != ' ':
					# Strings
					if char in ['"', "'"]:
						string = ""
						index = pos + 1
						curr_char = line[index]
						while curr_char not in ["'", '"']:
							if index > len(line):
								throw_error.error('Quote never closed', pos)
								return
							string += curr_char
							index += 1
							curr_char = line[index]
						tokenized_line.append(Token("STRING", string))
						continue_ = len(string) + 1
					# Change token's value to the text until next space
					else:
						word = line[pos:].split()[0]
						if word in list(builtins.keys()):
							tokenized_line.append(builtins[word])
						else:
							tokenized_line.append(Token("VAR", word))
							continue_ = len(word)
	if __name__ == "__main__":
		return ",\n".join([i.ID + " : " + str(i.value) for i in tokenized_line])
	else:
		return [(i.ID, i.value) for i in tokenized_line]


if __name__ == '__main__':
	print("Welcome to the lexer of felicity!")
	while True:
		line = input(">>> ")
		if line == "":
			break
		lexed_line = lex(line)
		if lexed_line != None:
			print(lexed_line)
