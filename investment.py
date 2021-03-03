def calculate_apr(principal,interest_rate,years):
	"""
	Calculates the growth of an investment with compound interest.

	This function takes in 3 parameters/arguments,
	and it checks whether the interest rate is a negative value with an if-statement.
	Then, it calculates the principal after each year based on a compound interest.
	"""
#	principal=input("Enter principal:")
#	principal=int(principal)
#	print(principal)
#	interest_rate=input("Enter interest rate:")
#	interest_rate=int(interest_rate)
	principal=500
	interest_rate=0.03
	years=0
#	print(f'The new principal after 1 year is {principal*(1+interest_rate)}')

	if interest_rate<0.00:
		print("False")
		exit()
	else:
#		principal*(1+interest_rate)
		while years<65:
			principal=principal*(1+interest_rate)
#		print(f'After year {years}, the new principal is {principal}')
			years+=1

	return principal
#	print(f'On the {years}th year, the principal has become {principal}')
