def calculator(number1,number2,operator):
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
	else:
		exit()

def input_output():
	dec = 'y'
	oper = ''
	while dec == 'y':
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
			break
