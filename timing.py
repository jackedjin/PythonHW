import time
def calculate_time(func):
	def wrapper_calculatetime():
		start = time.time()
		func()
		time.sleep(2)
		stop = time.time()
		X=stop-start
		print(f'Total time taken is {X} seconds')
	return wrapper_calculatetime
