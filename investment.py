def calculate_apr(principal,interest_rate,years):
	"""
	Calculates the growth of an investment with compound interest.

	This function takes in 3 parameters/arguments,
	and it checks whether the interest rate is a negative value with an if-statement.
	Then, it calculates the principal after each year based on a compound interest.
	"""
	if interest_rate<0:
		return str(false)
		exit()

	principal=500
	interest_rate=0.03
	years=0

#	if interest_rate<0:
#		return str(false)
#		exit()
#	else:
#		principal*(1+interest_rate)
	while years<65:
		principal=principal*(1+interest_rate)
#		print(f'After year {years}, the new principal is {principal}')
		years+=1
		new_principal = float("{:.7f}".format(principal))
		return new_principal

#	if interest_rate<0:
#		return str(false)
#		exit()
#	print(f'On the {years}th year, the principal has become {principal}')
