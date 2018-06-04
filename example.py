

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



def calc(exp, i):
	operand = Stack()
	operator = Stack()
	while True:
		print(exp[i], " ", i)
		if (exp[i].isdigit()):
			operand.push(exp[i])
			i =i+ 1
		elif(exp[i] == "/" or exp[i] == "*" or exp[i] == "+" or exp[i] == "-" ):
			
			if operator.isEmpty():
				operator.push(exp[i])
				i=i+1
	

	

				

ans = calc(expr1, 0)




