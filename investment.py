def calculate_apr(principal,interest_rate,years):
	"""
	Calculates the growth of an investment with compound interest.

	This function takes in 3 parameters/arguments,
	and it checks whether the interest rate is a negative value with an if-statement.
	Then, it calculates the principal after each year based on a compound interest.
	"""

	if principal<0 or interest_rate<=0 or years<0:
#or principal<0 or years<0:
		exit()
	return false

	else:
#		principal=principal*(1+interest_rate)
		x=0
		while x<years:
			principal=principal*(1+interest_rate)
			x+=1
			new_principal = float("{:.7f}".format(principal))

	return new_principal
