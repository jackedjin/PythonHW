def calculator(number1,number2,operator):
	"""
	This function accepts 3 parameters - number1, number2 and operator, and it checks for the type of operator, and returns the respective result from the arithmetic operation
	"""
	if operator=='+': 
		return number1+number2
	elif operator=='-':
		return number1-number2
	elif operator=='*':
		return number1*number2
	elif operator=='/':
		return number1/number2
	elif operator=='**':
		return number1**number2
	elif operator=='//':
		return number1//number2
	else: #if its any other character or string, exit immediately
		exit()

def input_output():
	"""
	This function runs on a while loop and prompts user to enter the following parameters - number1, number2 and operator. Upon receiving the parameters, the function calls the calculator function from above,
	passes the parameters into the calculator function which checks the operator and returns the result which is then printed. This is followed by prompting the user if they wish to continue.
	If 'y' is entered, the user can continue with the mathemetical operation, however, if it is a 'n', it breaks the loop and exits.
	"""
	dec = 'y'
	oper = ''
	while dec == 'y': #loops until 'n' is entered by user
		num1=input("Enter number1:")
		num1=int(num1)
		print(num1)
		num2=input("Enter number2:")
		num2=int(num2)
		print(num2)
		oper=input("Enter operator:")
		print(oper)
		result=calculator(num1,num2,oper)
		print(result)
		dec=input("Enter 'y' to continue or 'n' to exit:")
		if dec == 'n':
			break #breaks the loop
