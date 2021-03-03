import time
def calculate_time(func):
	def wrapper_calculate_time():
		start = time.time()
		func()
		time.sleep(2)
		stop = time.time()
		print(f'Total time taken is {stop-start} seconds')
		return wrapper_calculate_time
