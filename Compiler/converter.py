class Dictionary:
	def __init__(self, name, line):
		self.name = name
		self.is_main = isMain()
		if self.is_main:
			self.execute()
		else:
			self.is_conventions = isConventions()
			self.conventions()

	def isMain():
		if self.name == "main":
			return True

	def isConventions():
		if self.name == "conventions":
			return True


def converter(file):
	pass
	#builtins = ["if", "else-if", "else", "not", "{", "}"]
	# for line in file:
	# 	if "{" in line:
	# 		name_pos
	#		locals()[line.index("{")-1] = Dictionary()