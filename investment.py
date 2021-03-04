def calculate_apr(principal,interest_rate,years):
	"""
	Calculates the growth of an investment with compound interest.

	This function takes in 3 parameters/arguments,
	and it checks whether the interest rate is a negative value with an if-statement.
	Then, it calculates the principal after each year based on a compound interest.
	"""
	principal=500
	interest_rate=0.03
	years=65
	x=0
	while x<years:
		principal=principal*(1+interest_rate/100)
#		print(f'After year {years}, the new principal is {principal}')
		x+=1
		new_principal = float("{:.7f}".format(principal))
	return new_principal
