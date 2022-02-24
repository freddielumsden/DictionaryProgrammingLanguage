import throw_error

def checkBraces(file_split):
	for pos, line in enumerate(file_split):
		if line[-1] == '{':
			expected_tab_number = line[0].count('\t') + 1
			index = pos
			inside_of_list = True
			while inside_of_list:
				index += 1
				tab_count = file_split[index][0].count('\t')
				if tab_count == expected_tab_number - 1:
					# The string index of the first character after tabs is tab_count*2
					# because the tab character is \t, which is two characters,
					# and it would be -1 to get the last character of tab,
					# as the element index starts at 0, but to get one more,
					# you must +1 which cancels -1.
					try:
						if file_split[index][0][tab_count] == "}":
							inside_of_list = False
					except:	
						throw_error.error("The brace was never closed", pos, file_split, pos=line.index('{'))
						break
				elif index > len(file_split) or tab_count < expected_tab_number:
					throw_error.error("The brace was never closed", pos, file_split, pos=line.index('{'))
					break


def lexer(file):
	file_split = [i.split(' ') for i in file.split('\n')]
	check_braces = checkBraces(file_split)
	if check_braces != None:
		return check_braces
