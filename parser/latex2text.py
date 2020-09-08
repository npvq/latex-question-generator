import re

class ParserError(Exception):
	pass

backslash = "\\"
openbracket = "{"
closebracket = "}"

latex_functions = [
	"sin", "cos", "tan", "cot", "sec", "csc",
	"arcsin", "arccos", "arctan", "arccot", "arcsec", "arccsc",
	"log"
]

latex_constants = [
	"pi"
]

latex_special = {
	"frac": lambda x: x
}

def f_backslash(chars):
	if not chars:
		raise ParserError
	
	if chars[0] == backslash:
		chars.pop(0)
#	else:
#		print("WARNING: \"f_backslash\": There was no backslash >:( ")

	command = ""
	inner = ""

	while chars:
		x = chars.pop(0)
		if x == openbracket:
			break
		command += x

	bracket_depth = 0
	while chars:
		x = chars.pop(0)
		if x == closebracket:
			if not bracket_depth:
				break
			else:
				bracket_depth -= 1
		elif x == openbracket:
			bracket_depth += 1
		inner += x

	return (chars, command, inner)

def convert(chars):
	output = ""
	while chars:
		x = chars.pop(0)
		if x == backslash:
			chars, command, inner = f_backslash(chars)
			if inner in :
				output += f"{command}({convert(list(inner))})"
			else:
				output += f"{command}"
		else:
			output += x
	return output


# MAIN FUNCTION

def latex2text(input):
	return convert(list(input))



if __name__ == "__main__":
	print("Testing...")
	print(latex2text(r"\frac{1}{2}"))

#EOF