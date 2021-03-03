def calculate_apr():
	principal=input("Enter principal:")
	principal=int(principal)
	print(principal)
	interest_rate=input("Enter interest rate:")
	interest_rate=int(interest_rate)
	if interest_rate<0:
		print("False")
		exit()
	else:
		print(interest_rate)
	years=input("Enter number of years:")
	years=int(years)
	print(years)

	for x in range(years):
		principal=principal*(1+interest_rate/100)
		print(f'After year {x}, the new principal is {principal}')
		x+=1

	print(f'On the {x}th year, the principal has become {principal}')
