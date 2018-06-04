

from Stack import Stack
import re

expr = input("Please enter an expression to calculate:")

expr1 = re.split('([0-9]+)|\s', expr)

while "" in expr1 or None in expr1:
	if "" in expr1:
		expr1.remove("")
	elif None in expr1:
		expr1.remove(None)
	 

print(expr1)




def calc(expr, i, space):
	operand = Stack()
	operators = Stack()
	while True:
		if (expr[i].isalpha()):
			operand.push(expr[i])
					

if " " in list(expr):
	x = calc(expr, i, True)

	print(expr.split())
else:
	x = calc(expr, i, False)




