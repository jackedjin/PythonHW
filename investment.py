def calculate_apr(principal,interest_rate,years):
	"""
	Calculates the growth of an investment with compound interest.

	This function takes in 3 parameters/arguments,
	and it checks whether the interest rate is a negative value with an if-statement.
	Then, it calculates the principal after each year based on a compound interest.
	"""
	principal=100
	interest_rate=0.06
	years=65

	one_year=principal*(1+interest_rate)
	if interest_rate<0:
		return false
		exit()
	else:
		x=0
		while x<years:
			principal=principal*(1+interest_rate/100)
#			print(f'After year {years}, the new principal is {principal}')
			x+=1
			new_principal = float("{:.7f}".format(principal))
	return_list=[oneyear,new_principal]

	return return_list
