def calculate_apr(principal,interest_rate,years):
#	principal=input("Enter principal:")
#	principal=int(principal)
#	print(principal)
#	interest_rate=input("Enter interest rate:")
#	interest_rate=int(interest_rate)
	principal=500
	interest_rate=0.03
	years=65
	x=1
	print(f'The new principal after 1 year is {principal*(1+interest_rate)}')

	if interest_rate<0.00:
		print("False")
		exit()
	for x in range(1,years):
		principal=principal*(1+interest_rate)
#		print(f'After year {x}, the new principal is {principal}')
		x+=1

	print(f'On the {x}th year, the principal has become {principal}')
