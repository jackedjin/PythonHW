import time
	"""
	imports current time
	"""

def calculate_time(func):
	"""
	decorator function which accepts another function as an argument, and is passed into the wrapper function which calculates the start and end time of running a function,
	and printing the difference.
	"""
	def wrapper_calculatetime():
		start = time.time() #the start time of the function
		func() #function passed as an argument
#		time.sleep(1)
		stop = time.time() #the stop time of the function
		X=stop-start
		print(f'Total time {X}')
	return wrapper_calculatetime
