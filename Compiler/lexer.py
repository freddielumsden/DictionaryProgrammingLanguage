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
					if file_split[index][0][(tab_count * 2)-1] == "}":
						inside_of_list = False
				elif index > len(file_split) or tab_count < expected_tab_number:
					return "Error: The brace was never closed Ln " + str(pos)


def lexer(file):
	file_split = [i.split(' ') for i in file.split('\n')]
	check_braces = checkBraces(file_split)
	if check_braces != None:
		return check_braces
	return file_split
