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
	oneyear=0

	if interest_rate<0:
		exit

#	one_year=principal*(1+interest_rate)

#	if interest_rate<0:
#		return false
#		exit()
	else:
		oneyear=principal*(1+interest_rate)
		x=0
		while x<years:
			principal=principal*(1+interest_rate/100)
			x+=1
			new_principal = float("{:.7f}".format(principal))

	one_year=float("{:.7f}".format(oneyear))
	return_list=[one_year,new_principal]

	return return_list
