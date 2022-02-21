def getConventions(file):
	file_line_number = 0
	file_line = file[file_line_number]
	conventions = []
	while file_line[0:9] == "convention":
		conventions += file_line[10:-2]
		file_line_number += 1
		file_line = file_line[file_line_number]
	return conventions, file_line_number

def getMainPos(file, ignore_up_to):
	file_line_number = ignore_up_to
	file_line = file[file_line_number]
	while file_line_number < len(file):
		file_line_number += 1
		file_line = file[file_line_number]
		if "main" in file:
			start = file_line_number
			break
	while 
	return None

def converter(file):
	getConventions = getConventions()
	conventions = getConventions[0]
	ignore_up_to = getConventions[1]
	keywords = {"main", "for", "if", "elif", "else", "while", "using", "convention"}
	main = {}
	main_positions = {}
	main_pos = getMainPos(file, ignore_up_to)
	for line in file[main_pos + 1]:
		for word in line:
			pass
